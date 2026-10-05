/* Canvas movement: native scrolling, pointer sorting, and keyboard sorting. */
(() => {
  "use strict";
  const board = document.getElementById("kanbanBoard");
  const canvas = document.getElementById("kanbanCanvas");
  const feedback = document.getElementById("kanbanFeedback");
  if (!board || !canvas) return;
  let pending = null;
  let drag = null;
  let frame = 0;
  let holdTimer = 0;
  const columns = () => [...board.querySelectorAll("[data-kanban-status]")];
  const cardsIn = (column) =>
    [...(column?.querySelectorAll("[data-project-id]") || [])].filter(
      (card) => card !== drag?.card,
    );
  const announce = (message) => {
    feedback.textContent = message;
  };
  const clearMarkers = () =>
    board
      .querySelectorAll(
        ".is-drop-target, .kanban-drop-before, .kanban-drop-after",
      )
      .forEach((element) =>
        element.classList.remove(
          "is-drop-target",
          "kanban-drop-before",
          "kanban-drop-after",
        ),
      );
  const closeDropdowns = () =>
    board.querySelectorAll("select").forEach((field) => {
      if (window.jQuery?.(field).data("select2")?.isOpen())
        window.jQuery(field).select2("close");
    });
  canvas.addEventListener("scroll", closeDropdowns, { passive: true });

  function setDestination(column, index = 0) {
    if (!drag) return;
    const cards = cardsIn(column);
    index = Math.max(0, Math.min(index, cards.length));
    if (drag.target === column && drag.index === index) return;
    clearMarkers();
    drag.target = column;
    drag.index = index;
    drag.beforeId = cards[index]?.dataset.projectId || null;
    if (!column) return;
    column.classList.add("is-drop-target");
    if (cards[index]) cards[index].classList.add("kanban-drop-before");
    else cards.at(-1)?.classList.add("kanban-drop-after");
    announce(`Tujuan: ${column.dataset.kanbanStatus}, urutan ${index + 1}.`);
  }

  function begin(card, mode) {
    closeDropdowns();
    const column = card.closest("[data-kanban-status]");
    const initialIndex = [
      ...column.querySelectorAll("[data-project-id]"),
    ].indexOf(card);
    drag = {
      card,
      mode,
      id: card.dataset.projectId,
      name: card.querySelector("h3").textContent,
      target: null,
      index: -1,
      beforeId: null,
      point: null,
      preview: null,
    };
    card.classList.add("is-dragging");
    document.body.classList.add("kanban-dragging");
    setDestination(column, initialIndex);
    if (mode === "pointer") {
      drag.preview = document.createElement("div");
      drag.preview.className = "kanban-drag-preview";
      drag.preview.setAttribute("aria-hidden", "true");
      drag.preview.textContent = drag.name;
      document.body.append(drag.preview);
    } else
      announce(
        `${drag.name} diambil. Kiri/kanan memilih kolom; atas/bawah mengatur urutan; Enter meletakkan; Escape membatalkan.`,
      );
  }

  function finish(cancel = false) {
    clearTimeout(holdTimer);
    const current = drag;
    const pointerId = pending?.kind === "pointer" ? pending.id : null;
    pending = null;
    drag = null;
    cancelAnimationFrame(frame);
    frame = 0;
    if (pointerId !== null && board.hasPointerCapture(pointerId))
      board.releasePointerCapture(pointerId);
    document.body.classList.remove("kanban-dragging");
    clearMarkers();
    if (!current) return;
    current.card.classList.remove("is-dragging");
    current.preview?.remove();
    if (!cancel && current.target) {
      board.dispatchEvent(
        new CustomEvent("kanban:move", {
          detail: {
            id: current.id,
            status: current.target.dataset.kanbanStatus,
            beforeId: current.beforeId,
          },
        }),
      );
    } else announce("Pemindahan dibatalkan.");
    if (current.card.isConnected) current.card.focus({ preventScroll: true });
  }

  function updatePointer(x, y) {
    if (!drag) return;
    drag.point = { x, y };
    drag.preview.style.left = `${Math.max(8, Math.min(x + 16, innerWidth - 246))}px`;
    drag.preview.style.top = `${Math.max(8, Math.min(y + 16, innerHeight - drag.preview.offsetHeight - 8))}px`;
    const column = document
      .elementFromPoint(x, y)
      ?.closest("[data-kanban-status]");
    if (!column || !board.contains(column)) {
      setDestination(null);
      return;
    }
    const cards = cardsIn(column);
    const before = cards.findIndex((card) => {
      const rect = card.getBoundingClientRect();
      return y < rect.top + rect.height / 2;
    });
    setDestination(column, before < 0 ? cards.length : before);
  }

  function scrollEdges() {
    if (!drag?.point || drag.mode !== "pointer") return;
    const { x, y } = drag.point;
    const rect = canvas.getBoundingClientRect();
    const speed = (value, start, end) =>
      value < start + 48 ? -10 : value > end - 48 ? 10 : 0;
    if (
      x >= rect.left &&
      x <= rect.right &&
      y >= rect.top &&
      y <= rect.bottom
    ) {
      canvas.scrollBy(
        speed(x, rect.left, rect.right),
        speed(y, rect.top, rect.bottom),
      );
      updatePointer(x, y);
    }
    frame = requestAnimationFrame(scrollEdges);
  }
  function movePointer(x, y) {
    updatePointer(x, y);
    if (!frame) frame = requestAnimationFrame(scrollEdges);
  }
  function draggableCard(target) {
    if (
      target.closest(
        "button, a, input, select, label, textarea, .select2-container",
      )
    )
      return null;
    return target.closest("[data-project-id]");
  }

  board.addEventListener("pointerdown", (event) => {
    if (
      event.pointerType === "touch" ||
      event.button !== 0 ||
      !event.isPrimary ||
      drag
    )
      return;
    const card = draggableCard(event.target);
    if (!card) return;
    event.preventDefault();
    card.focus({ preventScroll: true });
    pending = {
      kind: "pointer",
      id: event.pointerId,
      card,
      x: event.clientX,
      y: event.clientY,
    };
  });
  document.addEventListener(
    "pointermove",
    (event) => {
      if (pending?.kind !== "pointer" || event.pointerId !== pending.id) return;
      if (!drag) {
        if (
          Math.hypot(event.clientX - pending.x, event.clientY - pending.y) < 6
        )
          return;
        begin(pending.card, "pointer");
        board.setPointerCapture(event.pointerId);
      }
      event.preventDefault();
      movePointer(event.clientX, event.clientY);
    },
    { passive: false },
  );
  document.addEventListener("pointerup", (event) => {
    if (pending?.kind !== "pointer" || event.pointerId !== pending.id) return;
    if (drag) updatePointer(event.clientX, event.clientY);
    finish();
  });
  document.addEventListener("pointercancel", (event) => {
    if (pending?.kind === "pointer" && pending.id === event.pointerId)
      finish(true);
  });
  board.addEventListener("lostpointercapture", () => {
    if (pending?.kind === "pointer" && drag) finish(true);
  });
  board.addEventListener("dragstart", (event) => event.preventDefault());

  // Short swipes remain native scrolling; only a stationary long press starts dragging.
  board.addEventListener(
    "touchstart",
    (event) => {
      if (event.touches.length !== 1) {
        finish(true);
        return;
      }
      if (drag) return;
      const card = draggableCard(event.target);
      if (!card) return;
      const touch = event.touches[0];
      pending = {
        kind: "touch",
        id: touch.identifier,
        card,
        x: touch.clientX,
        y: touch.clientY,
      };
      holdTimer = setTimeout(() => {
        if (pending?.kind !== "touch") return;
        begin(card, "pointer");
        movePointer(pending.x, pending.y);
      }, 350);
    },
    { passive: true },
  );
  document.addEventListener(
    "touchmove",
    (event) => {
      if (pending?.kind !== "touch") return;
      const touch = [...event.touches].find(
        (item) => item.identifier === pending.id,
      );
      if (!touch || event.touches.length !== 1) {
        finish(true);
        return;
      }
      if (!drag) {
        if (
          Math.hypot(touch.clientX - pending.x, touch.clientY - pending.y) > 8
        )
          finish(true);
        return;
      }
      if (event.cancelable) event.preventDefault();
      movePointer(touch.clientX, touch.clientY);
    },
    { passive: false },
  );
  document.addEventListener("touchend", (event) => {
    if (pending?.kind !== "touch") return;
    const touch = [...event.changedTouches].find(
      (item) => item.identifier === pending.id,
    );
    if (!touch) return;
    if (drag) updatePointer(touch.clientX, touch.clientY);
    finish();
  });
  document.addEventListener("touchcancel", () => {
    if (pending?.kind === "touch") finish(true);
  });
  board.addEventListener("contextmenu", (event) => {
    if (drag || pending?.kind === "touch") event.preventDefault();
  });

  board.addEventListener("keydown", (event) => {
    // Child fields keep their own keyboard controls.
    const card = event.target.closest("[data-project-id]");
    if (!card || event.target !== card) return;
    const confirm = event.key === "Enter" || event.key === " ";
    if (!drag && confirm) {
      event.preventDefault();
      begin(card, "keyboard");
      return;
    }
    if (drag?.mode !== "keyboard") return;
    if (confirm) {
      event.preventDefault();
      finish();
    } else if (
      ["ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"].includes(event.key)
    ) {
      event.preventDefault();
      if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
        const areas = columns();
        const next = Math.max(
          0,
          Math.min(
            areas.length - 1,
            areas.indexOf(drag.target) + (event.key === "ArrowLeft" ? -1 : 1),
          ),
        );
        setDestination(areas[next], drag.index);
      } else
        setDestination(
          drag.target,
          drag.index + (event.key === "ArrowUp" ? -1 : 1),
        );
      const cards = cardsIn(drag.target);
      (cards[drag.index] || cards.at(-1) || drag.target).scrollIntoView({
        block: "nearest",
        inline: "nearest",
      });
    } else if (event.key === "Tab") finish(true);
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && (drag || pending)) {
      event.preventDefault();
      finish(true);
    }
  });
  window.addEventListener("blur", () => {
    if (drag || pending) finish(true);
  });
  document.addEventListener("visibilitychange", () => {
    if (document.hidden && (drag || pending)) finish(true);
  });
})();

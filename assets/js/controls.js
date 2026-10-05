/* Shared enhancements preserve the original fields, names and form values. */
(() => {
  "use strict";
  const $ = window.jQuery;
  const icon = (name) =>
    `<svg aria-hidden="true" viewBox="0 0 24 24">${window.BRUTAL_ICONS[name]}</svg>`;
  const selects = new Set();
  const dates = new Set();

  function enhanceSelect(field) {
    if (selects.has(field) || field.hasAttribute("data-native")) return;
    const restoreFocus = document.activeElement === field;
    selects.add(field);
    const existing = $(field).data("select2");
    if (!existing) {
      const width = field.classList.contains("w-auto")
        ? `${Math.max(130, field.getBoundingClientRect().width)}px`
        : "100%";
      $(field).select2({
        width,
        dropdownParent: $(field.closest(".modal") || document.body),
        minimumResultsForSearch: field.options.length > 8 ? 0 : Infinity,
        language: { noResults: () => "Tidak ada pilihan yang cocok." },
      });
    }
    const container = $(field).data("select2").$container[0];
    const selection = container.querySelector(".select2-selection");
    const label =
      field.getAttribute("aria-label") ||
      [...field.labels].map((el) => el.textContent.trim()).join(" ") ||
      "Pilih opsi";
    selection.removeAttribute("aria-labelledby");
    selection.setAttribute("aria-label", label);
    selection.setAttribute("aria-required", String(field.required));
    container
      .querySelector(".select2-search__field")
      ?.setAttribute("aria-label", label);
    if (field.hasAttribute("aria-describedby"))
      selection.setAttribute(
        "aria-describedby",
        field.getAttribute("aria-describedby"),
      );
    field.addEventListener("focus", () => selection.focus());
    for (const labelElement of field.labels) {
      labelElement.addEventListener("click", (event) => {
        event.preventDefault();
        if (!field.disabled) selection.focus();
      });
    }
    field.addEventListener("invalid", (event) => {
      event.preventDefault();
      selection.setAttribute("aria-invalid", "true");
      // Native validation fires for every invalid control: focus only the first.
      if (field.form?.querySelector(":invalid") === field) selection.focus();
    });
    // Select2 emits jQuery events; bridge them for existing vanilla JS handlers.
    $(field).on("change.neo", (event) => {
      selection.setAttribute("aria-invalid", String(!field.validity.valid));
      if (!event.originalEvent && !event.namespace)
        field.dispatchEvent(new Event("change", { bubbles: true }));
    });
    $(field).on("select2:open.neo", () => {
      const search = $(field)
        .data("select2")
        .$dropdown[0].querySelector(".select2-search__field");
      if (search) {
        search.setAttribute("aria-label", `Cari ${label}`);
        search.placeholder = "Ketik untuk mencari…";
      }
    });
    if (restoreFocus) selection.focus();
  }

  function enhanceDate(field) {
    if (
      field._flatpickr ||
      field.readOnly ||
      field.disabled ||
      field.hasAttribute("data-native")
    )
      return;
    dates.add(field);
    const type = field.type;
    const format =
      type === "time"
        ? "H:i"
        : type === "datetime-local"
          ? "Y-m-d\\TH:i"
          : "Y-m-d";
    const probe = document.createElement("input");
    probe.type = type;
    for (const attribute of ["min", "max", "step", "required"]) {
      if (field.hasAttribute(attribute))
        probe.setAttribute(attribute, field.getAttribute(attribute));
    }
    const validate = () => {
      for (const attribute of ["min", "max", "step", "required"]) {
        if (field.hasAttribute(attribute))
          probe.setAttribute(attribute, field.getAttribute(attribute));
        else probe.removeAttribute(attribute);
      }
      probe.value = field.value;
      field.setCustomValidity(
        (field.value && !probe.value) || !probe.validity.valid
          ? "Isi tanggal atau waktu yang valid sesuai rentang yang ditentukan."
          : "",
      );
    };
    const picker = flatpickr(field, {
      locale: flatpickr.l10ns.id,
      dateFormat: format,
      allowInput: true,
      disableMobile: true,
      enableTime: type !== "date",
      noCalendar: type === "time",
      time_24hr: true,
      minuteIncrement: 1,
      monthSelectorType: "static",
      minDate: type === "time" ? undefined : field.min || undefined,
      maxDate: type === "time" ? undefined : field.max || undefined,
      minTime: type === "time" ? field.min || undefined : undefined,
      maxTime: type === "time" ? field.max || undefined : undefined,
      appendTo: field.closest(".modal") || document.body,
      prevArrow: icon("chevron-left"),
      nextArrow: icon("chevron-right"),
      onChange: validate,
      onOpen: (_dates, _value, instance) => {
        if (field.readOnly || field.disabled) {
          instance.close();
          return;
        }
        validate();
        if (field.validity.valid || !field.value)
          instance.setDate(field.value, false, format);
        const today = instance.calendarContainer.querySelector(
          ".neo-calendar-footer button",
        );
        if (today) today.disabled = !instance.isEnabled(new Date());
        field.setAttribute("aria-expanded", "true");
      },
      onClose: () => field.setAttribute("aria-expanded", "false"),
    });
    field.classList.add("neo-date-input");
    field.placeholder ||=
      type === "time"
        ? "HH:MM"
        : type === "datetime-local"
          ? "YYYY-MM-DDTHH:MM"
          : "YYYY-MM-DD";
    field.setAttribute("aria-haspopup", "dialog");
    field.setAttribute("aria-expanded", "false");
    field.setAttribute("aria-controls", `${field.id}-calendar`);
    picker.calendarContainer.id = `${field.id}-calendar`;
    picker.calendarContainer.setAttribute("role", "dialog");
    picker.calendarContainer.setAttribute(
      "aria-label",
      type === "time" ? "Pilih waktu" : "Pilih tanggal",
    );
    for (const [node, label, offset] of [
      [picker.prevMonthNav, "Bulan sebelumnya", -1],
      [picker.nextMonthNav, "Bulan berikutnya", 1],
    ]) {
      if (!node) continue;
      node.setAttribute("role", "button");
      node.setAttribute("tabindex", "0");
      node.setAttribute("aria-label", label);
      node.addEventListener("keydown", (event) => {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          picker.changeMonth(offset);
        }
      });
    }
    const footer = document.createElement("div");
    footer.className = "neo-calendar-footer";
    for (const [label, action] of [
      [
        type === "time" ? "Sekarang" : "Hari ini",
        () => {
          const now = new Date();
          if (!picker.isEnabled(now)) return;
          picker.setDate(now, true);
          picker.close();
          field.focus();
        },
      ],
      [
        "Bersihkan",
        () => {
          picker.clear();
          picker.close();
          field.focus();
        },
      ],
    ]) {
      const button = document.createElement("button");
      button.type = "button";
      button.className = "btn btn-sm";
      button.textContent = label;
      button.addEventListener("click", action);
      footer.append(button);
    }
    picker.calendarContainer.append(footer);
    // Focus restoration must not reopen a just-closed calendar.
    picker.set("clickOpens", false);
    field.addEventListener("click", () => {
      if (!field.readOnly && !field.disabled) picker.open();
    });
    field.addEventListener(
      "keydown",
      (event) => {
        if (event.key === "Escape" && picker.isOpen) {
          event.stopImmediatePropagation();
          picker.close();
        }
        if (event.key === "ArrowDown") {
          event.preventDefault();
          event.stopImmediatePropagation();
          picker.open();
          const day =
            picker.selectedDateElem ||
            picker.todayDateElem ||
            picker.calendarContainer.querySelector(
              ".flatpickr-day:not(.flatpickr-disabled):not(.prevMonthDay):not(.nextMonthDay)",
            );
          (type === "time" ? picker.hourElement : day)?.focus();
        }
        if (event.key === "Enter") {
          validate();
          if (!field.validity.valid) {
            event.preventDefault();
            event.stopImmediatePropagation();
            field.reportValidity();
          }
        }
      },
      true,
    );
    picker.calendarContainer.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        event.stopPropagation();
        picker.close();
        field.focus();
      }
    });
    // Flatpickr accepts overflow dates (e.g. 31 February). Keep invalid typed
    // values visible so native constraint feedback can explain the problem.
    field.addEventListener(
      "blur",
      (event) => {
        validate();
        if (!field.validity.valid && field.value)
          event.stopImmediatePropagation();
      },
      true,
    );
    field.addEventListener("input", validate);
    field.addEventListener("change", validate);
  }

  function enhance(root) {
    if (!(root instanceof Element || root instanceof Document)) return;
    const all = (selector) => [
      ...(root.matches?.(selector) ? [root] : []),
      ...root.querySelectorAll(selector),
    ];
    all("select.form-select").forEach(enhanceSelect);
    all(
      'input[type="date"], input[type="time"], input[type="datetime-local"]',
    ).forEach(enhanceDate);
  }
  enhance(document);
  // Dynamic Kanban fields and plugin-generated table controls use the same skin.
  new MutationObserver((records) => {
    for (const field of selects) {
      if (!field.isConnected) {
        $(field).off(".neo");
        $(field).select2("destroy");
        selects.delete(field);
      }
    }
    for (const field of dates) {
      if (!field.isConnected) {
        field._flatpickr.destroy();
        dates.delete(field);
      }
    }
    for (const record of records)
      for (const node of record.addedNodes) enhance(node);
  }).observe(document.body, { childList: true, subtree: true });
  document.addEventListener("reset", (event) => {
    setTimeout(() => {
      event.target.querySelectorAll("select").forEach((field) => {
        if ($(field).data("select2")) {
          $(field).trigger("change.select2");
          $(field).data("select2").$selection.removeAttr("aria-invalid");
        }
      });
      event.target.querySelectorAll(".neo-date-input").forEach((field) => {
        field._flatpickr.setDate(field.value, false);
        field.setCustomValidity("");
      });
    }, 0);
  });
  document.addEventListener("hide.bs.modal", (event) => {
    event.target.querySelectorAll("select").forEach((field) => {
      if ($(field).data("select2")) $(field).select2("close");
    });
    event.target
      .querySelectorAll(".neo-date-input")
      .forEach((field) => field._flatpickr.close());
  });
})();

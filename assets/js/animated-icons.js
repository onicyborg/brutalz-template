/* Interactive Lordicon gallery. Assets are embedded to also support file://. */
(() => {
  const triggerControl = document.getElementById("animatedTrigger");
  if (!triggerControl) return;

  const speedControl = document.getElementById("animatedSpeed");
  const pauseButton = document.getElementById("animatedPause");
  const status = document.getElementById("animatedStatus");
  const icons = [...document.querySelectorAll("lord-icon[data-icon]")];
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
  let paused = false;
  const inView = new Set();
  const failed = new Set();
  const originals = new Map();

  function chosenTrigger(icon) {
    if (!icon.dataset.defaultTrigger) return "";
    return triggerControl.value === "default"
      ? icon.dataset.defaultTrigger
      : triggerControl.value;
  }

  function syncPlayback(icon) {
    const trigger = chosenTrigger(icon);
    const held =
      paused || document.hidden || reducedMotion.matches || !inView.has(icon);
    const active = held ? "" : trigger;
    if (icon.getAttribute("trigger") !== active) {
      if (active) icon.setAttribute("trigger", active);
      else icon.removeAttribute("trigger");
    }
    if (held) {
      // Settle the explicit demo's promise when playback is interrupted.
      if (icon.dataset.defaultTrigger) icon.pause();
      else icon.stop();
    }
  }

  function update() {
    icons.forEach((icon) => {
      icon.setAttribute("speed", speedControl.value);
      syncPlayback(icon);
      const card = icon.closest(".animated-icon-card");
      if (!card) return;
      const trigger = chosenTrigger(icon);
      const automatic = trigger.startsWith("loop");
      card.querySelector(".animated-mode").textContent = automatic
        ? "Otomatis"
        : trigger === "hover"
          ? "Hover"
          : "Klik";
      const hint = failed.has(icon)
        ? "Ikon gagal dimuat. Muat ulang halaman untuk mencoba lagi."
        : paused
          ? "Animasi dijeda. Tekan Lanjutkan untuk mencoba."
          : reducedMotion.matches
            ? "Mode gerakan terbatas aktif: ikon ditampilkan statis."
            : automatic
              ? "Diputar berulang dengan jeda selama ikon terlihat."
              : trigger === "hover"
                ? "Arahkan kursor, fokuskan, atau tekan ikon."
                : "Klik, sentuh, atau tekan Enter / Space pada ikon.";
      card.querySelector(".animated-hint").textContent = hint;
      const snippet = originals
        .get(icon)
        .replace(/trigger="[^"]*"/, `trigger="${trigger}"`)
        .replace('target="', `speed="${speedControl.value}" target="`);
      card.querySelector("code").textContent = snippet;
      card.querySelector(".icon-copy").dataset.copy = snippet;
    });
    pauseButton.setAttribute("aria-pressed", String(paused));
    pauseButton.textContent = paused
      ? "Lanjutkan animasi"
      : "Jeda semua animasi";
    status.textContent = reducedMotion.matches
      ? "Preferensi reduced motion aktif. Animasi ditampilkan statis."
      : paused
        ? "Semua animasi dijeda."
        : "Animasi aktif. Coba ikon dengan pemicu yang dipilih.";
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(({ target, isIntersecting }) => {
        if (isIntersecting) inView.add(target);
        else inView.delete(target);
        syncPlayback(target);
      });
    },
    { threshold: 0.1 },
  );

  icons.forEach((icon) => {
    const card = icon.closest(".animated-icon-card");
    if (card)
      originals.set(icon, card.querySelector(".icon-copy").dataset.copy);
    icon.addEventListener("error", () => {
      failed.add(icon);
      update();
      if (!card)
        document.getElementById("animatedEventStatus").textContent =
          "Ikon gagal dimuat. Muat ulang halaman.";
    });
    icon.addEventListener("ready", () => syncPlayback(icon));
    // No fetch: a fresh object protects the shared source from player mutations.
    icon.icon = structuredClone(
      window.BRUTAL_ANIMATED_ICONS[icon.dataset.icon],
    );
    observer.observe(icon);
    card
      ?.querySelector(".animated-icon-target")
      .addEventListener("click", () => {
        if (paused || reducedMotion.matches || failed.has(icon)) return;
        // Native click trigger already handles mouse, touch, Enter, and Space.
        if (chosenTrigger(icon) === "hover") icon.play({ from: "start" });
      });
  });

  triggerControl.addEventListener("change", update);
  speedControl.addEventListener("change", update);
  pauseButton.addEventListener("click", () => {
    paused = !paused;
    update();
  });
  reducedMotion.addEventListener("change", update);
  document.addEventListener("visibilitychange", () =>
    icons.forEach(syncPlayback),
  );
  document
    .getElementById("animatedEventButton")
    .addEventListener("click", async () => {
      const icon = document.getElementById("animatedEventIcon");
      const feedback = document.getElementById("animatedEventStatus");
      if (paused || reducedMotion.matches) {
        feedback.textContent = paused
          ? "Lanjutkan animasi terlebih dahulu."
          : "Simulasi selesai. Mode gerakan terbatas aktif.";
        return;
      }
      if (failed.has(icon)) {
        feedback.textContent = "Ikon gagal dimuat. Muat ulang halaman.";
        return;
      }
      feedback.textContent = "Memutar animasi unduhan…";
      try {
        const completed = await icon.play({ from: "start" });
        feedback.textContent = completed
          ? "Simulasi selesai!"
          : "Animasi dihentikan.";
      } catch (_) {
        feedback.textContent =
          "Animasi belum tersedia. Coba muat ulang halaman.";
      }
    });
  update();
})();

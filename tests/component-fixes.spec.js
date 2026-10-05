const { test, expect } = require("@playwright/test");
const { choose } = require("./helpers/controls");

async function withinViewport(page, locator) {
  const box = await locator.boundingBox();
  expect(box.x).toBeGreaterThanOrEqual(0);
  expect(box.x + box.width).toBeLessThanOrEqual(page.viewportSize().width);
  expect(
    await page.evaluate(
      () => document.documentElement.scrollWidth <= innerWidth,
    ),
  ).toBe(true);
}

for (const width of [1440, 390, 320]) {
  test(`Select2 single and multiple popups fit at ${width}px, including search and clear`, async ({
    page,
  }) => {
    await page.setViewportSize({ width, height: 900 });
    await page.goto("/forms-advanced-form.html");
    const team = page.locator("#advancedTeam + .select2-container");
    await team.click();
    await withinViewport(page, page.locator(".select2-dropdown"));
    const trigger = await team.boundingBox();
    const popup = await page.locator(".select2-dropdown").boundingBox();
    expect(Math.abs(trigger.width - popup.width)).toBeLessThan(2);
    await page
      .locator(".select2-search--dropdown input")
      .fill("No matching team");
    await expect(page.locator(".select2-results__message")).toContainText(
      "Tidak ada tim",
    );
    await page.keyboard.press("Escape");
    await team.locator(".select2-selection").press("Enter");
    await page
      .locator(".select2-search--dropdown input")
      .pressSequentially("Engineering");
    await expect(
      page.getByRole("option", { name: "Tim Engineering", exact: true }),
    ).toBeVisible();
    await page.keyboard.press("Enter");
    await expect(page.locator("#advancedTeam")).toHaveValue("Tim Engineering");
    await team.locator(".select2-selection__clear").click();
    await page.locator(".select2-search--dropdown input").press("Escape");
    await expect(page.locator(".select2-dropdown")).toHaveCount(0);
    await expect(page.locator("#advancedTeam")).toHaveValue("");
    const skills = page.locator("#advancedSkills + .select2-container");
    await skills.click();
    await withinViewport(page, page.locator(".select2-dropdown"));
    await page.getByRole("option", { name: "Desain UI", exact: true }).click();
    await skills.locator("input").fill("Frontend");
    await page.getByRole("option", { name: "Frontend", exact: true }).click();
    await expect(skills.locator(".select2-selection__choice")).toHaveCount(2);
    await skills.locator("input").press("Backspace");
    await expect(skills.locator(".select2-selection__choice")).toHaveCount(1);
    await page.keyboard.press("Escape");
    await page.getByRole("button", { name: "Reset", exact: true }).click();
    await expect(skills.locator(".select2-selection__choice")).toHaveCount(0);
  });
}

test("enhanced selects support keyboard, labels, reset, optgroups and disabled options", async ({
  page,
}) => {
  await page.goto("/basic-form.html");
  await page.locator('label[for="role"]').click();
  await expect(
    page.locator("#role + .select2-container .select2-selection"),
  ).toBeFocused();
  await page.mouse.move(0, 0);
  await page.keyboard.press("Enter");
  await page.keyboard.press("ArrowDown");
  await page.keyboard.press("Enter");
  await expect(page.locator("#role")).toHaveValue("Designer");
  await page.getByRole("button", { name: "Reset", exact: true }).click();
  await expect(page.locator("#role + .select2-container")).toContainText(
    "Pilih peran",
  );
  await page.locator("#demoForm").evaluate((form) => {
    const label = document.createElement("label");
    label.htmlFor = "groupFixture";
    label.textContent = "Tim contoh";
    const select = document.createElement("select");
    select.className = "form-select";
    select.id = "groupFixture";
    select.innerHTML =
      '<optgroup label="Desain"><option>UI</option><option disabled>UX</option></optgroup><optgroup label="Teknik" disabled><option>Backend</option></optgroup>';
    form.append(label, select);
  });
  await page.locator("#groupFixture + .select2-container").click();
  await expect(
    page.getByRole("option", { name: "UX", exact: true }),
  ).toHaveAttribute("aria-disabled", "true");
  await expect(
    page.getByRole("option", { name: "Backend", exact: true }),
  ).toHaveAttribute("aria-disabled", "true");
  await page.keyboard.press("Escape");
  await page.locator("#groupFixture").evaluate((select) => {
    select.disabled = true;
  });
  await expect(
    page.locator("#groupFixture + .select2-container .select2-selection"),
  ).toHaveAttribute("aria-disabled", "true");
});

test("project modal keeps dropdown and calendar keyboard focus inside the dialog", async ({
  page,
}) => {
  await page.setViewportSize({ width: 320, height: 900 });
  await page.goto("/projects.html");
  await page.getByRole("button", { name: "Proyek baru", exact: true }).click();
  await choose(page, page.locator("#projectCategory"), "Branding");
  await page.locator("#projectDue").click();
  const calendar = page.locator("#projectDue-calendar");
  await expect(calendar).toBeVisible();
  await withinViewport(page, calendar);
  await calendar
    .locator(
      ".flatpickr-day:not(.prevMonthDay):not(.nextMonthDay):not(.flatpickr-disabled)",
    )
    .filter({ hasText: /^15$/ })
    .click();
  await expect(page.locator("#projectDue")).toHaveValue(/^\d{4}-\d{2}-15$/);
  await page.locator("#projectDue").press("ArrowDown");
  await expect(calendar).toBeVisible();
  await page.keyboard.press("Escape");
  await expect(calendar).toBeHidden();
  await expect(page.locator("#projectModal")).toBeVisible();
  await page.getByRole("button", { name: "Batal", exact: true }).click();
  await expect(page.locator(".select2-dropdown")).toHaveCount(0);
});

test("date picker respects range, rejects impossible typed dates and resets cleanly", async ({
  page,
}) => {
  await page.goto("/basic-form.html");
  await page.locator("#startDate").fill("2026-02-31");
  await page.locator("#bio").click();
  await expect(page.locator("#startDate")).toHaveValue("2026-02-31");
  expect(
    await page.locator("#startDate").evaluate((field) => field.checkValidity()),
  ).toBe(false);
  await page.locator("#startDate").fill("2026-02-28");
  await page.locator("#bio").click();
  expect(
    await page.locator("#startDate").evaluate((field) => field.checkValidity()),
  ).toBe(true);
  await page.getByRole("button", { name: "Reset", exact: true }).click();
  await expect(page.locator("#startDate")).toHaveValue("");
  await page.locator("#demoForm").evaluate((form) => {
    const input = document.createElement("input");
    Object.assign(input, {
      id: "rangeFixture",
      type: "date",
      min: "2026-10-10",
      max: "2026-10-20",
      value: "2026-10-15",
      className: "form-control",
    });
    input.setAttribute("aria-label", "Rentang contoh");
    form.append(input);
  });
  await expect(page.locator("#rangeFixture")).toHaveClass(/neo-date-input/);
  await page.locator("#rangeFixture").click();
  await expect(
    page
      .locator("#rangeFixture-calendar .flatpickr-day")
      .filter({ hasText: /^9$/ }),
  ).toHaveClass(/flatpickr-disabled/);
  await expect(
    page
      .locator("#rangeFixture-calendar .flatpickr-day")
      .filter({ hasText: /^21$/ }),
  ).toHaveClass(/flatpickr-disabled/);
  await page
    .locator("#rangeFixture-calendar")
    .getByRole("button", { name: "Bersihkan" })
    .click();
  await expect(page.locator("#rangeFixture")).toHaveValue("");
});

test("time picker remains editable with a visible clear action inside the calendar modal", async ({
  page,
}) => {
  await page.goto("/calendar.html");
  await page.getByRole("button", { name: "Agenda baru" }).click();
  await page.locator("#eventTime").click();
  const popup = page.locator("#eventTime-calendar");
  await expect(popup).toBeVisible();
  await popup.locator(".flatpickr-hour").fill("14");
  await popup.locator(".flatpickr-minute").fill("35");
  await popup.locator(".flatpickr-minute").press("Tab");
  await expect(page.locator("#eventTime")).toHaveValue("14:35");
  await popup.getByRole("button", { name: "Bersihkan" }).click();
  await expect(page.locator("#eventTime")).toHaveValue("");
});

test("progress stripes move, pause, resume and respect reduced motion", async ({
  page,
}) => {
  await page.goto("/progress.html");
  const bar = page.locator(".progress-bar-animated");
  const position = () =>
    bar.evaluate((el) => getComputedStyle(el).backgroundPositionX);
  expect(
    await bar.evaluate((el) => getComputedStyle(el).backgroundImage),
  ).toContain("linear-gradient");
  const initial = await position();
  await expect.poll(position).not.toBe(initial);
  await page.locator("#progressAnimation").click();
  await expect(page.locator("#progressAnimation")).toHaveAttribute(
    "aria-pressed",
    "true",
  );
  await expect(bar).toHaveCSS("animation-play-state", "paused");
  await page.locator("#progressAnimation").click();
  await expect(bar).toHaveCSS("animation-play-state", "running");
  await page.emulateMedia({ reducedMotion: "reduce" });
  await expect(bar).toHaveCSS("animation-name", "none");
});

test("pagination uses SVG navigation and dynamic lists update disabled boundaries", async ({
  page,
}) => {
  for (const [url, id, next, previous] of [
    [
      "basic-table",
      "tablePagination",
      "Halaman berikutnya",
      "Halaman sebelumnya",
    ],
    ["blog", "blogPagination", "Artikel berikutnya", "Artikel sebelumnya"],
  ]) {
    await page.goto(`/${url}.html`);
    const nav = page.locator(`#${id}`);
    await expect(nav.getByRole("button", { name: previous })).toBeDisabled();
    await expect(
      nav.getByRole("button", { name: next }).locator("svg"),
    ).toHaveCount(1);
    await nav.getByRole("button", { name: next }).click();
    await expect(nav.getByRole("button", { name: previous })).toBeEnabled();
    await nav.getByRole("button", { name: previous }).click();
    await expect(nav.getByRole("button", { name: previous })).toBeDisabled();
  }
});

test("navbar input group stays joined on mobile and tabs follow navigation direction", async ({
  page,
}) => {
  await page.setViewportSize({ width: 320, height: 900 });
  await page.goto("/navbar.html");
  const input = page.getByRole("searchbox", { name: "Cari di navbar contoh" });
  await input.fill("Studio");
  await page
    .locator(".navbar-demo-search")
    .getByRole("button", { name: "Cari" })
    .click();
  await expect(page.locator("#navbarSearchResult")).toContainText("Studio");
  const left = await input.boundingBox();
  const right = await page.locator(".navbar-demo-search button").boundingBox();
  expect(Math.abs(left.y - right.y)).toBeLessThan(1);
  expect(Math.abs(left.x + left.width - right.x)).toBeLessThanOrEqual(2);
  await page.setViewportSize({ width: 1440, height: 900 });
  await page.goto("/tabs.html");
  await expect(page.locator(".tab-content--bottom")).toHaveCSS(
    "border-top-left-radius",
    "6px",
  );
  await expect(page.locator(".tab-content--left")).toHaveCSS(
    "border-top-left-radius",
    "0px",
  );
  await expect(page.locator(".tab-content--right")).toHaveCSS(
    "border-top-right-radius",
    "0px",
  );
  await page.locator("#tabsLeft-tab-0").press("ArrowDown");
  await expect(page.locator("#tabsLeft-tab-1")).toHaveAttribute(
    "aria-selected",
    "true",
  );
});

test("gallery focus has smooth feedback and reduced motion removes movement", async ({
  page,
}) => {
  await page.goto("/light-gallery.html");
  const tile = page.locator(".media-tile").first();
  await tile.focus();
  await expect(tile).toHaveCSS("transition-duration", "0.2s, 0.2s");
  await expect(tile).toHaveCSS("box-shadow", "rgb(35, 36, 32) 6px 6px 0px 0px");
  await page.emulateMedia({ reducedMotion: "reduce" });
  await expect(tile).toHaveCSS("transform", "none");
});

test("an empty calendar supports complete keyboard selection and rejects invalid Enter input", async ({
  page,
}) => {
  await page.goto("/basic-form.html");
  const field = page.locator("#startDate");
  await field.focus();
  await page.keyboard.press("ArrowDown");
  await expect(
    page.locator("#startDate-calendar .flatpickr-day:focus"),
  ).toHaveCount(1);
  await page.keyboard.press("ArrowRight");
  await page.keyboard.press("Enter");
  await expect(field).toHaveValue(/^\d{4}-\d{2}-\d{2}$/);
  await field.fill("2026-02-31");
  await field.press("Enter");
  await expect(field).toHaveValue("2026-02-31");
  expect(await field.evaluate((input) => input.checkValidity())).toBe(false);
});

// Select by value through the visible widget, retaining native fallback coverage.
async function choose(page, locator, value) {
  const field = locator.and(page.locator("select"));
  const option = await field.evaluate(
    (select, value) => ({
      id: select.id,
      text: [...select.options].find((option) => option.value === value)
        ?.textContent,
      enhanced: select.classList.contains("select2-hidden-accessible"),
    }),
    value,
  );
  if (!option.enhanced) return field.selectOption(value);
  await page
    .locator(`[id="${option.id}"] + .select2-container .select2-selection`)
    .click();
  await page.getByRole("option", { name: option.text, exact: true }).click();
}
module.exports = { choose };

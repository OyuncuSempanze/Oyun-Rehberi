(() => {
  const input = document.querySelector("#archive-search");
  const cards = Array.from(document.querySelectorAll(".game-card"));
  if (!input || cards.length === 0) return;

  const count = document.querySelector("#archive-count");
  const emptyState = document.querySelector("#archive-empty");
  const filterButtons = Array.from(document.querySelectorAll(".archive-filter[data-filter]"));
  let activeFilter = "all";

  const normalize = (value) => value
    .toLocaleLowerCase("tr-TR")
    .normalize("NFD")
    .replace(/[\u0300-\u036f]/g, "");

  const updateResults = () => {
    const query = normalize(input.value.trim());
    let visibleCount = 0;

    cards.forEach((card) => {
      const searchableText = normalize(
        `${card.dataset.search || ""} ${card.textContent || ""}`
      );
      const matchesQuery = searchableText.includes(query);
      const matchesCategory = activeFilter === "all" || card.dataset.category === activeFilter;
      const matches = matchesQuery && matchesCategory;

      card.hidden = !matches;
      if (matches) visibleCount += 1;
    });

    if (count) {
      count.textContent = visibleCount === 1 ? "1 oyun" : `${visibleCount} oyun`;
    }

    if (emptyState) {
      emptyState.hidden = visibleCount !== 0;
    }
  };

  filterButtons.forEach((button) => {
    button.addEventListener("click", () => {
      activeFilter = button.dataset.filter || "all";

      filterButtons.forEach((filterButton) => {
        const selected = filterButton === button;
        filterButton.classList.toggle("is-active", selected);
        filterButton.setAttribute("aria-pressed", String(selected));
      });

      updateResults();
    });
  });

  input.addEventListener("input", updateResults);
})();

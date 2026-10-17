(() => {
  const input = document.querySelector("#archive-search");
  const cards = Array.from(document.querySelectorAll(".game-card"));
  if (!input || cards.length === 0) return;

  const count = document.querySelector("#archive-count");
  const emptyState = document.querySelector("#archive-empty");

  const updateResults = () => {
    const query = input.value.trim().toLocaleLowerCase("tr-TR");
    let visibleCount = 0;

    cards.forEach((card) => {
      const searchableText = `${card.dataset.search || ""} ${card.textContent || ""}`.toLocaleLowerCase("tr-TR");
      const matches = searchableText.includes(query);
      card.hidden = !matches;
      if (matches) visibleCount += 1;
    });

    if (count) {
      count.textContent = `${visibleCount} oyun`;
    }
    if (emptyState) {
      emptyState.hidden = visibleCount !== 0;
    }
  };

  input.addEventListener("input", updateResults);
})();

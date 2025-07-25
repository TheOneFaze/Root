
document.addEventListener("DOMContentLoaded", function () {
    const searchIcon = document.querySelector(".search-icon");
    const searchContainer = document.querySelector(".search-container");
    const searchInput = document.getElementById("searchInput");
    const logo = document.getElementById("logo");

    let userOpenedSearch = false;

    if (searchIcon && searchContainer) {
        searchIcon.addEventListener("click", function (e) {
            e.stopPropagation();
            const isOpen = searchContainer.classList.toggle("active");
            userOpenedSearch = isOpen;

            if (isOpen) {
                setTimeout(() => searchInput.focus(), 100);
                logo?.classList.add("hidden-on-search-active");
                document.body.style.overflow = 'hidden'; // Prevent scroll on mobile
            } else {
                searchInput.value = "";
                searchInput.blur();
                logo?.classList.remove("hidden-on-search-active");
                document.body.style.overflow = ''; // Restore scroll
            }
        });

        // Prevent keyboard-resize collapse
        let lastHeight = window.innerHeight;
        window.addEventListener("resize", () => {
            if (userOpenedSearch) {
                const diff = Math.abs(window.innerHeight - lastHeight);
                if (diff < 200) return;
            }
            lastHeight = window.innerHeight;
        });

        document.addEventListener("click", function (e) {
            if (
                !searchContainer.contains(e.target) &&
                !searchIcon.contains(e.target) &&
                userOpenedSearch
            ) {
                searchContainer.classList.remove("active");
                logo?.classList.remove("hidden-on-search-active");
                userOpenedSearch = false;
                document.body.style.overflow = '';
            }
        });
    }
});

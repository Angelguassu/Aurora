document.getElementById('open_btn').addEventListener('click', function () {
    document.getElementById('sidebar').classList.toggle('open-sidebar');
});


document.addEventListener("DOMContentLoaded", () => {
    const sideItems = document.querySelectorAll(".side-item");
    const sections = {
        "Dashboard": document.getElementById("dashboard-section"),
        "Usuários": document.getElementById("usuarios-section"),
        "Calendar": document.getElementById("calendar-section"),
        "Produtos": document.getElementById("produtos-section"),
        "Imagens": document.getElementById("imagens-section"),
        "Configurações": document.getElementById("configuracoes-section")
    };

    sideItems.forEach(item => {
        item.addEventListener("click", (e) => {
            e.preventDefault();

            // Remove classe 'active' de todos os itens
            sideItems.forEach(i => i.classList.remove("active"));
            item.classList.add("active");

            // Pega o nome do menu clicado
            const label = item.querySelector(".item-description").textContent.trim();

            // Oculta todas as sections
            Object.values(sections).forEach(section => section.style.display = "none");

            // Exibe a section correspondente
            if (sections[label]) {
                sections[label].style.display = "block";
            }
        });
    });
});

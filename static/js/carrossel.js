document.addEventListener('DOMContentLoaded', function () {
    inicializarCarrossel('#banner');

});

function inicializarCarrossel(IdCarrossel) {
    var element = document.querySelector(IdCarrossel);
    if (!element) {
        console.error("Elemento com ID " + IdCarrossel + " não encontrado.");
        return; // Aborta a função se o elemento não for encontrado
    }

    if (element.classList.contains('is-initialized')) {
        return; // Evita a reinicialização do carrossel
    }

    element.classList.add('is-initialized'); // Marca o carrossel como inicializado

    var splide = new Splide(IdCarrossel, {
        type: 'slide',
        autoplay: true,
        speed: 500,
        pauseOnHover: false,
        perPage: 1,
        perMove: 1,
        rewind: true,
        rewindSpeed: 500,
        interval: 4000,
        arrows: true,
    });

    splide.mount();

    
}

// REMOVE AS "BOLINHAS" DE PAGINAÇÃO DO CARROSSEL 
document.addEventListener('DOMContentLoaded', function() {
    var paginationElements = document.querySelectorAll('.splide__pagination');
    paginationElements.forEach(function(element) {
        element.remove();
    });
});

const imgCardio7 = document.querySelector('#img-cardio-7')
const imgCardioCare2000 = document.querySelector('#img-cardio-care-2000')
const imgCardiotouch3000 = document.querySelector('#img-cardiotouch-3000')
const bm1 = document.querySelector('#img-bm1')
const bm3 = document.querySelector('#img-bm3')
const bm5 = document.querySelector('#img-bm5')


function trocaDeImagem(variavel, img1, img2) {
    variavel.addEventListener('mouseover', () => {
        // Inicia o fade out (esmaecimento)
        variavel.classList.add('opacity-0');
        
        // Após o fade out, troca a imagem e inicia o fade in
        setTimeout(() => {
            variavel.src = img1;
            variavel.classList.remove('opacity-0'); // Inicia o fade in
        }, 150); // Tempo de 500ms, igual ao tempo de transição definido no Tailwind
    });
    
    variavel.addEventListener('mouseleave', () => {
        // Inicia o fade out (esmaecimento)
        variavel.classList.add('opacity-0');
        
        // Após o fade out, troca a imagem e inicia o fade in
        setTimeout(() => {
            variavel.src = img2;
            variavel.classList.remove('opacity-0'); // Inicia o fade in
        }, 150); // Tempo de 500ms, igual ao tempo de transição definido no Tailwind
    });
}




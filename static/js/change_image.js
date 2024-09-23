const imgCardio7 = document.querySelector('#img-cardio-7')
const imgCardioCare2000 = document.querySelector('#img-cardio-care-2000')
const imgCardiotouch3000 = document.querySelector('#img-cardiotouch-3000')

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

trocaDeImagem(imgCardio7, 'https://i.postimg.cc/jjK6RFGH/Eletrocardi-grafo-Cardio7-Bionet-completo.jpg', 'https://s3.sa-east-1.amazonaws.com/macrosul.media/itens/eletrocardiografo/cardio7-dicom/I03368/eletrocardiografo-cardio7-dicom-bionet-I03368-5.png')

trocaDeImagem(imgCardioCare2000,'https://i.postimg.cc/HkZHmVvd/cardiocare-2000-acessorios.jpg','https://s3.sa-east-1.amazonaws.com/macrosul.media/itens/eletrocardiografo/cardiocare-2000/I04007/eletrocardiografo-cardiocare-2000-bionet-I04007-1.png')

trocaDeImagem(imgCardiotouch3000,'https://i.postimg.cc/BQSdvJK6/Eletrocardiografo-Cardio-Touch-3000-acessorios.jpg','https://s3.sa-east-1.amazonaws.com/macrosul.media/itens/eletrocardiografo/cardiotouch/I04145/eletrocardiografo-cardiotouch-bionet-I04145-1.png')



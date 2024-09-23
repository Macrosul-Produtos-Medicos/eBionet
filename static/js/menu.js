const home = document.querySelector('#home')
const produtos = document.querySelector('#produtos')
const suporte = document.querySelector('#suporte')
const contato = document.querySelector('#contato')

console.log("URL atual: " + window.location.href.split('/')[3]);
const url = window.location.href.split('/')[3];

document.addEventListener('DOMContentLoaded', function () {
    if(url == 'produtos'){
        produtos.classList.add('border-blue-600','text-blue-600')
        produtos.classList.remove('border-transparent')
    }
    else{
        produtos.classList.remove('border-blue-600','text-blue-600')
        produtos.classList.add('border-transparent')
    }


    if(url == 'contato'){
        contato.classList.add('border-blue-600','text-blue-600')
        contato.classList.remove('border-transparent')
    }
    else{
        contato.classList.remove('border-blue-600','text-blue-600')
        contato.classList.add('border-transparent')
    }


    if(url == 'suporte'){
        suporte.classList.add('border-blue-600','text-blue-600')
        suporte.classList.remove('border-transparent')
    }
    else{
        suporte.classList.remove('border-blue-600','text-blue-600')
        suporte.classList.add('border-transparent')
    }

    if(url == ''){
        home.classList.add('border-blue-600','text-blue-600')
        home.classList.remove('border-transparent')
    }
    else{
        home.classList.remove('border-blue-600','text-blue-600')
        home.classList.add('border-transparent')
    }
});


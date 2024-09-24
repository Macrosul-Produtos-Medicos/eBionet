function menuProdutos(){
    return{
        menuProdutos: false,
        menuMobile: false,
    }
}

const home = document.querySelector('#home')
const produtos = document.querySelector('#produtos')
const suporte = document.querySelector('#suporte')
const contato = document.querySelector('#contato')

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


const homeMobile = document.querySelector('#homeMobile')
const produtosMobile = document.querySelector('#produtosMobile')
const suporteMobile = document.querySelector('#suporteMobile')
const contatoMobile = document.querySelector('#contatoMobile')


document.addEventListener('DOMContentLoaded', function () {
    if(url == 'produtos'){
        produtosMobile.classList.add('bg-[#0073BE]','text-white')
        produtosMobile.classList.remove('text-[#2fa5f3]')
    }
    else{
        produtosMobile.classList.remove('bg-[#0073BE]','text-white')
        produtosMobile.classList.add('text-[#2fa5f3]')
    }


    if(url == 'contato'){
        contatoMobile.classList.add('bg-[#0073BE]','text-white')
        contatoMobile.classList.remove('text-[#2fa5f3]')
    }
    else{
        contatoMobile.classList.remove('bg-[#0073BE]','text-white')
        contatoMobile.classList.add('text-[#2fa5f3]')
    }


    if(url == 'suporte'){
        suporteMobile.classList.add('bg-[#0073BE]','text-white')
        suporteMobile.classList.remove('text-[#2fa5f3]')
    }
    else{
        suporteMobile.classList.remove('bg-[#0073BE]','text-white')
        suporteMobile.classList.add('text-[#2fa5f3]')
    }

    if(url == ''){
        homeMobile.classList.add('bg-[#0073BE]','text-white')
        homeMobile.classList.remove('text-[#2fa5f3]')
    }
    else{
        homeMobile.classList.remove('bg-[#0073BE]','text-white')
        homeMobile.classList.add('text-[#2fa5f3]')
    }
});

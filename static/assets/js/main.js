document.addEventListener("DOMContentLoaded", function () {
    const formCadastro = document.getElementyById("formCadastro");

    formCadastro.addEventListener("submit", function (e) {
        e.preventDefault();


        const dados = Object.fromEntries(
            new FormData(formCadastro)
        );

        console.log("Dados captutados:");
        console.log("Nome:", dados.nome);
        console.log("Email:", dados,email);
        console.log("Telefone:", dados.telefone);
        console.log(dados);
    });

});
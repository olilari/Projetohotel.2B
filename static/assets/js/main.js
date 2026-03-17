document.addEventListener("DOMContentLoaded", function () {
    const formCadastro = document.getElementyById("formCadastro");
  

    if (formCadastro) {

    formCadastro.addEventListener("submit", async (e) =>{
        e.preventDefault();


        const dados = Object.fromEntries(
            new FormData(formCadastro)
        );

        try{

         const resp = await fetch('/api/cadastrar', {
            method: 'POST',
            headers: (  'Content-Type': 'apllication/json' },



         )
    
        } catch (err){

            alert('Erro de comunicação com o servidor: ' + err);
        }

        console.log("Dados captutados:");
        console.log("Nome:", dados.nome);
        console.log("Email:", dados,email);
        console.log("Telefone:", dados.telefone);
        console.log(dados);
    });
    }
});
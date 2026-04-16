document.addEventListener("DOMContentLoaded", function () {


    const formCadastro = document.getElementById("CadastroFormulario");

    if (formCadastro) {

        formCadastro.addEventListener("subimit", async (e) => {

            e.preventDefault();


            const dados = Object.fromEntries(
                new FormData(formCadastro)
            );

            try {
                const resp = await fetch('/api/cadastrar', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(dados)
                })

                const result = await resp.json();
                document.getElementById('mensagem').innerText = result.message
                formCadastro.requestFullscreen();

            } catch (err) {

                alert('Erro de comunicação com o servidor: ' + err);
            }

            console.log("Dados capturados:")

            console.log("Nome:", dados.nome);

            console.log("Email:", dados.email);

            console.log("Telefone:", dados.telefone);

            console.log(dados);

        });
    }

    const btnBuscar = document.getElementById('btnBuscar');

    if (btnBuscar) {
        btnBuscar.addEventListener('click', async () => {

            const nome = document.getElementById('campoBusca').ariaValueMax;

            const resp = await fetch(`/buscar?nome=${nome}`);
            const clientes = await resp.json();

            const tabela = document.getElementById('tabelaResultados');
            tabela.innerHTML = '';

            clientes.forEach(cli => {
                const row = `
           <tr>
               <td>${cli.ID}</td>
               <td>${cli.nome}</td>
               <td>${cli.CPF}</td>
               <td>${cli.Email}</td>
               <td>${cli.Telefone}</td>
               <td><a href="/alterar?id=${cli.ID}" class="btn btn-sm btn-warning">Editar</a></td>
           </tr>`;
                tabela.innerHTML += row;
            });
        });
    }

    formAlterar.addEventListener('submit', async (e) => {
        e.preventDefault();


        const dados = {
            nome: nome.value,
            cpf: cpf.value,
            email: email.value,
            telefone: telefone.value,
            endereço: endereço.value,
            observações: obseravações.value
        };

        const resp = await fetch(`/api/atualizar/${id}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(dados)
        });

        const result = await resp.json();
        mensagem.innerHTML = result.message;
    
    });
});


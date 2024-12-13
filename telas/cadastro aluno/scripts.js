const API_URL = 'http://127.0.0.1:8000/api';

function mostrarFiltros() {
    const conteudo = document.getElementById('conteudo');
    conteudo.innerHTML = `
        <div class="mb-3">
            <h4 class="text-center">Filtrar Alunos</h4>
            <input type="text" id="filtroNome" class="form-control mt-2" placeholder="Nome do Aluno">
            <input type="text" id="filtroMatricula" class="form-control mt-2" placeholder="Matrícula">
            
            <div class="d-flex justify-content-between mt-2">
                <button class="btn btn-block btn-primary me-2" onclick="filtrarAlunos()">Filtrar</button>
                <button class="btn btn-block btn-secondary" onclick="listarTodosAlunos()">Listar Todos</button>
            </div>

            <button class="btn btn-block mt-2" style="background-color: #007bff; color: #fff;" onclick="limparFiltros()">Limpar</button>
        </div>

        <div id="resultadoAlunos" class="mt-3">
            <p class="text-center">Use os filtros acima para consultar alunos.</p>
        </div>
    `;
}

function limparFiltros() {
    document.getElementById('filtroNome').value = '';
    document.getElementById('filtroMatricula').value = '';
    const resultado = document.getElementById('resultadoAlunos');
    resultado.innerHTML = '<p class="text-center mt-3 text-muted">Filtros limpos.</p>';
}

async function filtrarAlunos() {
    const nome = document.getElementById('filtroNome').value;
    const matricula = document.getElementById('filtroMatricula').value;
    const resultado = document.getElementById('resultadoAlunos');

    resultado.innerHTML = '<p class="text-center">Buscando alunos...</p>';

    try {
        const queryParams = [];
        if (nome) queryParams.push(`nome=${encodeURIComponent(nome)}`);
        if (matricula) queryParams.push(`matricula=${encodeURIComponent(matricula)}`);

        const queryString = queryParams.join('&');
        const response = await fetch(`${API_URL}/alunos?${queryString}`);

        if (!response.ok) throw new Error('Erro ao buscar alunos.');

        const alunos = await response.json();
        if (alunos.length > 0) {
            renderizarAlunos(alunos, resultado);
        } else {
            resultado.innerHTML = '<p class="text-center mt-3 text-danger">Nenhum aluno encontrado.</p>';
        }
    } catch (error) {
        console.error('Erro ao filtrar alunos:', error);
        resultado.innerHTML = '<p class="text-danger mt-3">Erro ao buscar alunos.</p>';
    }
}

async function listarTodosAlunos() {
    const resultado = document.getElementById('resultadoAlunos');

    resultado.innerHTML = '<p class="text-center">Buscando todos os alunos...</p>';

    try {
        const response = await fetch(`${API_URL}/alunos`);
        if (!response.ok) throw new Error('Erro ao buscar alunos.');

        const alunos = await response.json();
        renderizarAlunos(alunos, resultado);
    } catch (error) {
        console.error('Erro ao listar todos os alunos:', error);
        resultado.innerHTML = '<p class="text-danger text-center">Erro ao buscar alunos. Tente novamente.</p>';
    }
}

function renderizarAlunos(alunos, container) {
    let htmlContent = '<ul class="list-group mt-3">';

    if (alunos.length > 0) {
        alunos.forEach(aluno => {
            htmlContent += `
                <li class="list-group-item d-flex justify-content-between align-items-center">
                    <div>
                        <strong>Nome:</strong> ${aluno.nome}<br>
                        <strong>Matrícula:</strong> ${aluno.matricula}
                    </div>

                    <div>
                        <button class="btn btn-editar btn-sm mt-2" onclick="editarAluno('${aluno.matricula}')">Editar</button>
                        <button class="btn btn-remover btn-sm mt-2" onclick="removerAluno('${aluno.matricula}')">Remover</button>
                    </div>
                </li>
            `;
        });
        htmlContent += '</ul>';
    } else {
        htmlContent += '<li class="list-group-item text-center">Nenhum aluno encontrado.</li>';
    }
    container.innerHTML = htmlContent;
}


function editarAluno(matricula) {
    alert(`Botão Editar clicado para matrícula: ${matricula}`);
}

async function removerAluno(matricula) {
    if (!confirm(`Tem certeza de que deseja remover o aluno com matrícula ${matricula}?`)) {
        return;
    }

    try {
        const response = await fetch(`${API_URL}/alunos/${matricula}/`, {
            method: 'DELETE',
        });

        if (response.ok) {
            alert('Aluno removido com sucesso.');
            listarTodosAlunos();  // Atualiza a lista de alunos
        } else {
            const result = await response.json();
            console.error('Erro ao remover aluno:', result);
            alert('Erro ao remover aluno. Mensagem: ' + JSON.stringify(result));
        }
    } catch (error) {
        console.error('Erro ao remover aluno:', error);
        alert('Erro ao remover aluno. Tente novamente.');
    }
}

function cadastrarAluno() {
    const conteudo = document.getElementById('conteudo');
    conteudo.innerHTML = `
        <div class="mt-3">
            <input type="text" placeholder="Nome Completo" class="form-control mt-2" />
            <input type="text" placeholder="Matrícula" class="form-control mt-2" />
            <input type="file" class="form-control mt-2" />
            <textarea placeholder="Características" rows="3" class="form-control mt-2"></textarea>
            <button class="btn btn-block mt-2" onclick="salvarAluno()">Salvar</button>
        </div>
    `;
}

async function salvarAluno() {
    const nome = document.querySelector('input[placeholder="Nome Completo"]').value;
    const matricula = document.querySelector('input[placeholder="Matrícula"]').value;
    const fotoInput = document.querySelector('input[type="file"]');
    const foto = fotoInput.files[0];

    if (!nome || !matricula || !foto) {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    const formData = new FormData();
    formData.append('nome', nome);
    formData.append('matricula', matricula);
    formData.append('foto', foto);

    try {
        const response = await fetch(`${API_URL}/alunos/`, {
            method: 'POST',
            body: formData
        });

        const result = await response.json();  // Tenta obter a resposta JSON do servidor

        if (response.ok) {
            alert('Aluno cadastrado corretamente.');
            console.log(result);  // Debug: Resposta do servidor
        } else {
            console.error('Erro no servidor:', result);
            alert('Erro ao cadastrar aluno. Mensagem: ' + JSON.stringify(result));
        }
    } catch (error) {
        console.error('Erro ao salvar aluno:', error);
        alert('Erro ao salvar aluno. Tente novamente.');
    }
}



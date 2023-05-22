const lista_de_filmes = [];
const generos = ["Romance", "Esforço", "Sombrio", "Bem-humorado", "Melancolia", "Aventura", "Temerosa", "Tenso", "Em busca de emoção", "Frio", "Romântico", "Paz", "Tesão", "Super-heróis", "Sonolento", "Séries", "Solitário", "Terror", "Brincalhão"];
const respostas = ["Sim", "Não"];

class Filme {
  constructor(nome, data, nota, genero1, pontuacao_algoritmo, recomendado) {
    this.nome = nome;
    this.data = data;
    this.nota = nota;
    this.genero1 = genero1;
    this.pontuacao_algoritmo = pontuacao_algoritmo;
    this.recomendado = false;
  }
}

function adicionar_filme(nome, data, nota, genero1, pontuacao_algoritmo, recomendado) {
  const novoFilme = new Filme(nome, data, nota, genero1, pontuacao_algoritmo, recomendado);
  lista_de_filmes.push(novoFilme);
}

// adicionando filmes (teste)

adicionar_filme("Mamãe Mia! Aqui vamos nós outra vez ", new Date(2002, 3, 20), 9.0, "Romance", 0, false);
adicionar_filme("Homem de Ferro 3", new Date(1982, 5, 25), 8.1, "Esforço", 0, false);
adicionar_filme("Desejo Sombrio", new Date(1993, 5, 9), 8.1, "Sombrio", 0, false);
adicionar_filme("O Grande Lebowski", new Date(1993, 5, 9), 8.1, "Bem-Humurado", 0, false);
adicionar_filme("O brilho Etreno de uma Mente sem Lembranças", new Date(1993, 5, 9), 8.1, "Melancolia", 0, false);
adicionar_filme("Indiana Jones e os Caçadores da Arca Perdida", new Date(1993, 5, 9), 8.1, "Aventura", 0, false);
adicionar_filme("O Babadook", new Date(1993, 5, 9), 8.1, "Temerosa", 0, false);
adicionar_filme("Corra", new Date(1993, 5, 9), 8.1, "Tenso", 0, false);
adicionar_filme("Caçadores de Emoção", new Date(1993, 5, 9), 8.1, "Em Buca de emoção", 0, false);
adicionar_filme("A Era do Gelo", new Date(1993, 5, 9), 8.1, "Frio", 0, false);
adicionar_filme("Amor à Segunda Vista", new Date(1993, 5, 9), 8.1, "Romântico", 0, false);
adicionar_filme("Divaldo: O Mensageiro da Paz", new Date(1993, 5, 9), 8.1, "Paz", 0, false);
adicionar_filme("Cinquenta tons de Cinza", new Date(1993, 5, 9), 8.1, "Tesão", 0, false);
adicionar_filme("Vingadores Ultimato", new Date(1993, 5, 9), 8.1, "Super Herois", 0, false);
adicionar_filme("Antes do Amanhecer", new Date(1993, 5, 9), 8.1, "Sonolento", 0, false);
adicionar_filme("Stranger Things", new Date(1993, 5, 9), 8.1, "Séries", 0, false);
adicionar_filme("Clube da Luta", new Date(1993, 5, 9), 8.1, "Solitário", 0, false);
adicionar_filme("O Iluminado", new Date(1993, 5, 9), 8.1, "Terror", 0, false);
adicionar_filme("Deadpool", new Date(1993, 5, 9), 8.1, "Brincalhão", 0, false);





// Interface para o usuário

console.log("[0] Romance");
console.log("[1] Esforço");
console.log("[2] Sombrio");
console.log("[3] Bem-humorado");
console.log("[4] Melancolia");
console.log("[5] Aventura");
console.log("[6] Temerosa");
console.log("[7] Tenso");
console.log("[8] Em busca de emoção");
console.log("[9] Frio");
console.log("[10] Romântico");
console.log("[11] Paz");
console.log("[12] Tesão");
console.log("[13] Super-heróis");
console.log("[14] Sonolento");
console.log("[15] Séries");
console.log("[16] Solitário");
console.log("[17] Terror");
console.log("[18] Brincalhão");

const genero_desejado1 = parseInt(prompt("Como você está se sentindo?\n"));

// Registrando os gêneros digitados pelo usuário

const generoEscolhido = generos[genero_desejado1];

// Prova real

console.log(`Verificando os gêneros registrados...\n`);
console.log(`Genero 1 ----> ${generoEscolhido}`);

function buscar_filme(genero_desejado1) {
  const pontuacao_lista = [];
  const lista_de_filmes_filtrada = lista_de_filmes.filter(filme => !filme.recomendado);

  for (let i = 0; i < lista_de_filmes_filtrada.length; i++) {
    let x;
    if (genero_desejado1 === lista_de_filmes_filtrada[i].genero1) {
      x = 1;
    } else {
      x = 0;
    }

    let z;
    if (lista_de_filmes_filtrada[i].data >= new Date(2022, 0, 1)) {
      z = 1;
    } else if (lista_de_filmes_filtrada[i].data <= new Date(2018, 11, 31)) {
      z = 0.9;
    } else {
      z = 0.8;
    }

    let p = (lista_de_filmes_filtrada[i].nota / 6) + x + z;
    p = p * 2.17;
    lista_de_filmes_filtrada[i].pontuacao_algoritmo = p;
    pontuacao_lista.push(p);
  }

  const maior_valor = Math.max(...pontuacao_lista);

  for (let x = 0; x < lista_de_filmes_filtrada.length; x++) {
    if (maior_valor === lista_de_filmes_filtrada[x].pontuacao_algoritmo) {
      lista_de_filmes_filtrada[x].recomendado = true;
      console.log(`Recomendamos o filme: ${lista_de_filmes_filtrada[x].nome}, sua pontuação é ${lista_de_filmes_filtrada[x].pontuacao_algoritmo}, o gênero do filme é: ${lista_de_filmes_filtrada[x].genero1}\n`);
    }
  }

  // Interface para o usuário
  console.log(`Você gostaria de refazer a busca? O mesmo filme não será recomendado novamente`);
  console.log(`[0] Sim`);
  console.log(`[1] Não`);
  const resposta = parseInt(prompt(`Digite o número: `));
  console.log(`\n`);
  const respostaTexto = respostas[resposta];
  if (respostaTexto === "Sim") {
    buscar_filme(genero_desejado1);
  } else {
    console.log(`Certo, obrigado por utilizar nossa ferramenta!`);
  }
}

buscar_filme(genero_desejado1);


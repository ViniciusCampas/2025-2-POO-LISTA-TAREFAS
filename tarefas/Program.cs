// See https://aka.ms/new-console-template for more information
using System;

Console.WriteLine("==== Sistema de Tarefas ====\n");

var operacoes = new Operacoes();

Console.WriteLine("Preenchendo dados da tarefa 01...");
var tarefa01 = new Tarefa
{
    Nome = "Fazer compras",
    Descricao = "Comprar arroz, feijão e frutas",
    DataCriacao = DateTime.Now,
    Status = 1,
    DataExecucao = null
};

Console.WriteLine("Inserindo dados no banco de dados...");
int idInserido = operacoes.Criar(tarefa01);
Console.WriteLine($"Dados inseridos com sucesso! Id gerado: {idInserido}\n");


Console.WriteLine("Alterando tarefa criada...");
var tarefaAlterada = new Tarefa
{
    Id = idInserido, // Usa o mesmo ID retornado
    Nome = "Fazer compras no mercado",
    Descricao = "Comprar arroz, feijão, frutas e leite",
    Status = 2, // Exemplo: 2 = concluída
    DataExecucao = DateTime.Now
};

operacoes.Alterar(tarefaAlterada);
Console.WriteLine("Tarefa alterada com sucesso!\n");

Console.WriteLine("Listando tarefas existentes no banco:\n");
var lista = operacoes.Listar();
foreach (var t in lista)
{
    Console.WriteLine($"ID: {t.Id} | Nome: {t.Nome} | Status: {t.Status} | Criada: {t.DataCriacao} | Execução: {t.DataExecucao}");
}


Console.WriteLine("\nExcluindo tarefa criada...");
operacoes.Excluir(idInserido);
Console.WriteLine("Tarefa excluída com sucesso!\n");
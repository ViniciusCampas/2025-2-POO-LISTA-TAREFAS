public class Operacoes{
    
    private string connectionString =" ";
    public int Criar(Tarefa tarefa){

        using(var conexao= new MySqlConnection(connectionString)){
            conexao.Open();
            string sql= @"INSERT INTO tarefa (nome, descricao, dataCriacao, status, dataExecucao)
                            VALUS (@nome, @descricao, @dataCriacao, @stats, @dataExecucao);
                            SELECT LAST_INSERT ID();"
            using (var cmd = new MySqlCommand(sql,conexao)){
                cmd.Parameters.AddWithValue("@nome",Tarefa.Nome);                     
                cmd.Parameters.AddWithValue("@descricao", Tarefa.Descricao); 
                cmd.Parameters.AddWithValue("@",Tarefa.DataCriacao);                     
                cmd.Parameters.AddWithValue("@",Tarefa.Status);                     
                cmd.Parameters.AddWithValue("@",Tarefa.DataExecucao);                     
            }
        }
        return 0;
    }

    public Tarefa Buscar (int id){
        return null;
    }

    public List <Tarefa> Listar(){
        return Array.empty<Tarefa>();
    }

    public void Alterar(Tarefa tarefa){

    }

    public void Excluir (int id){

    }
}
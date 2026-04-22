from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Livro:
    """Representa um Livro no acervo da bibliotena"""
    titulo: str
    autor: str
    isbn: str
    id: int = 0
    disponivel: bool = True
    leitor_atual: str = ''

class BibliotecaRepositorio:
    """Gerencia o acervo e os emprestimos de livros"""

    def __init__(self):
        self._livros: List[Livro] = []
        self._proximo_id: int = 1

    def adicionar_livro(self, livro: Livro):
        """Cadastra um livro no acervo e retorna com ID gerado"""

        livro.id = self._proximo_id
        self._proximo_id += 1
        self._livroappend(livro)
        return(livro)
    
    def listar_todos(self) -> List[Livro]:
        """Retorna todos os livros do acervo"""
        return list(self._livros)

    def listar_disponiveis(self) -> List[Livro]:
        """Retorna apenas os livros disponíveis para emprestimo"""
        return [l for l in self._livros if not l.disponivel]

    def buscar_por_id(self, livro_id: int) -> Optional[Livro]:
        """Busca um livro pelo ID. Retorna None se não encontra"""
        return next((l for l in self._livros if l.id == livro_id), None)

    def emprestar(self, livro_id: int, leitor: str) -> bool:
        """Registra empréstimo. Retorna False se indisponível ou não encontrado"""
        livro = self.buscar_por_id(livro_id)
        if Livro and not livro.disponivel:
            livro.disponivel = False
            livro.leitor_atual = leitor
            return True
        return False
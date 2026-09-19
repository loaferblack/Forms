class SistemaReservaQuadras:
    def __init__(self):
        # Lista simulada de quadras disponíveis em Lages/SC
        self.quadras = [
            {"id": 1, "nome": "Quadra Sintética Bairro Coral", "esporte": "Futebol", "preco_hora": 100.0},
            {"id": 2, "nome": "Arena Esportiva Centro", "esporte": "Futebol / Vôlei", "preco_hora": 120.0},
            {"id": 3, "nome": "Quadra Poliesportiva Copacabana", "esporte": "Basquete / Futsal", "preco_hora": 80.0}
        ]
        self.reservas = []

    def listar_quadras(self):
        print("\n--- Quadras Disponíveis em Lages/SC ---")
        for q in self.quadras:
            print(f"[{q['id']}] {q['nome']} - Esporte: {q['esporte']} - R$ {q['preco_hora']}/hora")

    def fazer_reserva(self, cliente, quadra_id, horario):
        quadra_selecionada = next((q for q in self.quadras if q['id'] == quadra_id), None)
        
        if quadra_selecionada:
            reserva = {
                "cliente": cliente,
                "quadra": quadra_selecionada['nome'],
                "horario": horario
            }
            self.reservas.append(reserva)
            print(f"\nSucesso! Reserva confirmada para {cliente} na {quadra_selecionada['nome']} às {horario}.")
        else:
            print("\nErro: Quadra não encontrada.")

    def listar_reservas(self):
        print("\n--- Reservas Realizadas ---")
        if not self.reservas:
            print("Nenhuma reserva registrada.")
        for r in self.reservas:
            print(f"Cliente: {r['cliente']} | Quadra: {r['quadra']} | Horário: {r['horario']}")

# Exemplo de uso do sistema
if __name__ == "__main__":
    app = SistemaReservaQuadras()
    
    # Mostra as quadras
    app.listar_quadras()
    
    # Simula uma reserva feita pelo usuário
    app.fazer_reserva("Pablo Wolff", 1, "Terça-feira às 20:00")
    
    # Exibe as reservas cadastradas
    app.listar_reservas()
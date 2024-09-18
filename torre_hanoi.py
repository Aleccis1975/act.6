class TorreDeHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.varillas = {
            'A': list(reversed(range(1, num_discos + 1))),  # Discos en la varilla A
            'B': [],  # Varilla vacía
            'C': []   # Varilla vacía
        }

    def mover_disco(self, origen, destino):
        if len(self.varillas[origen]) == 0:
            return False, "La varilla de origen está vacía."
        if len(self.varillas[destino]) > 0 and self.varillas[destino][-1] < self.varillas[origen][-1]:
            return False, "No puedes mover un disco más grande sobre uno más pequeño."

        # Mover disco
        disco = self.varillas[origen].pop()
        self.varillas[destino].append(disco)
        return True, f"Disco {disco} movido de {origen} a {destino}"

    def verificar_reto(self, torre_destino):
        # Verifica si todos los discos están en la varilla destino
        return len(self.varillas[torre_destino]) == self.num_discos

    def reiniciar(self):
        # Reinicia el estado de las varillas, moviendo todos los discos a la varilla A
        self.varillas['A'] = list(reversed(range(1, self.num_discos + 1)))
        self.varillas['B'] = []
        self.varillas['C'] = []

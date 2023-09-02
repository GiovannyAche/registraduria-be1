from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Modelos.Resultado import Resultado
class ControladorResultado():
    def __init__(self):
        self.repositorioResultado = RepositorioResultado()
        self.repositorioCadidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
    def index(self):
        return self.repositorioResultado.findAll()
    def create(self,infoResultado):
        nuevoResultado=Resultado(infoResultado)
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    def update(self,id,infoResultado):
        ResultadoActual=Resultado(self.repositorioResultado.findById(id))
        ResultadoActual.numvotos = infoResultado["numvotos"]
        return self.repositorioResultado.save(ResultadoActual)
    def delete(self,id):
        return self.repositorioResultado.delete(id)

    def asignarCandidatoyMesa(self, id, id_candi, id_mesa):
        resultadoActual = Resultado(self.repositorioResultado.findById(id))
        CandidatoActual = Candidato(self.repositorioCadidato.findById(id_candi))
        MesaActual = Mesa(self.repositorioMesa.findById(id_mesa))
        resultadoActual.candidato = CandidatoActual
        resultadoActual.mesa = MesaActual
        return self.repositorioResultado.save(resultadoActual)
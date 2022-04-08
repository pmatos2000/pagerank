import axios from "axios";
import React, { useState } from "react";
import "./App.css";

interface IPagina {
  titulo: string;
  texto: string;
  url: string;
}

interface IResultado {
  peso: number;
  pagina: IPagina;
}

function App() {
  const [texto, setTexto] = useState("");
  const [resultado, setResultado] = useState<IResultado[]>([]);
  const [buscando, setBuscando] = useState(false);

  const onClickPesquisar = async () => {
    setBuscando(true);
    const resposta = await axios
      .get<IResultado[]>(`https://localhost:5000/busca?busca=${texto}`)
      .then((r) => r && r?.data)
      .catch((e) => []);
    console.log(resposta);
    setResultado(resposta);
    setBuscando(false);
  };
  return (
    <div className="App">
      <header className="App-header">
        <h1>Buscador</h1>
        <div style={{ display: "flex" }}>
          <input
            type="text"
            onChange={(e) => setTexto(e.target.value)}
            value={texto}
          />
          <button onClick={onClickPesquisar}>Pesquisar</button>
        </div>
        <div>
          {resultado.map((p, index) => {
            return (
              <div key={index}>
                <h4>{p.pagina.titulo}</h4>
                <h5>{p.pagina.texto.substring(0, 255)}</h5>
              </div>
            );
          })}
        </div>
      </header>
    </div>
  );
}

export default App;

document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("peliculaForm");
  const tableBody = document
    .getElementById("peliculasTable")
    .querySelector("tbody");
  let isUpdating = false;

  //async permite que la función se comporte de manera asíncrona,
  //puede ejecutar operaciones sin bloquear el hilo principal de ejecucion
  const fetchPeliculas = async () => {
    //luego cambiaremos la url por https://<hostdepanywhere>/productos
    const response = await fetch("http://127.0.0.1:5000//peliculas"); // promesa: esperar a que se complete la solicitud HTTP
    const peliculas = await response.json(); //esperar a que se complete la conversión de la respuesta a JSON
    tableBody.innerHTML = "";
    peliculas.forEach((pelicula) => {
      const row = document.createElement("tr");
      row.innerHTML = `
                <td>${pelicula.id}</td>
                <td>${pelicula.titulo}</td>
                <td>${pelicula.anioEstreno}</td>
                <td>${pelicula.categoriaId}</td>
                <td>${pelicula.duracion}</td>
                <td>
                    <button onclick="editProducto(${pelicula.id}, '${pelicula.titulo}', ${pelicula.anioEstreno}, ${pelicula.categoriaId}, ${pelicula.duracion})">Editar</button>
                    <button onclick="deleteProducto(${pelicula.id})">Eliminar</button>
                </td>
            `;
      tableBody.appendChild(row);
    });
  };

  const addPelicula = async (pelicula) => {
    await fetch("http://127.0.0.1:5000//agregar_pelicula", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(pelicula),
    });
    fetchPeliculas();
  };

  const updatePelicula = async (id, pelicula) => {
    await fetch(`http://127.0.0.1:5000//actualizar_pelicula//${id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(pelicula),
    });
    fetchPeliculas();
  };

  const deletePelicula = async (id) => {
    await fetch(`http://127.0.0.1:5000//eliminar_pelicula//${id}`, {
      method: "DELETE",
    });
    fetchPeliculas();
  };

  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const id = document.getElementById("id").value;
    const titulo = document.getElementById("titulo").value;
    const anioEstreno = document.getElementById("anioEstreno").value;
    const categoriaId = document.getElementById("categoriaId").value;
    const duracion = document.getElementById("duracion").value;
    const pelicula = { titulo, anioEstreno, categoriaI, duracion }; // {"nombre": <<nombre>> , "cantidad":<<cantidad>>, "precio":precio}

    if (isUpdating) {
      updatePelicula(id, pelicula);
      isUpdating = false;
    } else {
      addPelicula(pelicula);
    }

    form.reset();
    document.getElementById("id").value = "";
  });

  window.editPelicula = (id, titulo, anioEstreno, categoriaId, duracion) => {
    document.getElementById("id").value = id;
    document.getElementById("titulo").value = titulo;
    document.getElementById("anioEstreno").value = anioEstreno;
    document.getElementById("categoriaId").value = categoriaId;
    document.getElementById("duracion").value = duracion;
    isUpdating = true;
  };

  window.deletePelicula = (id) => {
    if (confirm("¿Estás seguro de eliminar esta película?")) {
      deletePelicula(id);
    }
  };

  fetchPelicula();
});

import "./App.css";
import { useState, useEffect } from "react";
import axios from "axios";


function App() {
  const [todos, updateTodos] = useState("");
  const [input, setInput] = useState("");
  const [fetchData, setFetchData] = useState(false);
  const baseUrl = "http://localhost:5000";
  const getDataUrl = `${baseUrl}/data`;
  const createDataUrl = `${baseUrl}/create`;
  const deleteDataUrl = `${baseUrl}/delete/`;

  const getData = async () => {
    try {
      const { data } = await axios.get(getDataUrl);
      updateTodos(data.data);
      setFetchData(false)
      console.log(todos);
      return data;
    } catch (error) {
      console.error({ message: "failed fetching data.", error });
    }
  };

  useEffect(() => {
      getData();
  }, []);

  useEffect(() => {
    if ( fetchData ) {
      getData();
    }
  }, [fetchData, getData]);

  const createData = async (inputText) => {
    try {
      const { data } = await axios.post(createDataUrl, { todo: inputText });
      console.log({ message: "posted data", data });
      setFetchData(true)
      return data;
    } catch (error) {
      console.error({ message: "failed creating data.", error });
    }
  };

  const deleteData = async (id) => {
    try {
      const { data } = await axios.delete(deleteDataUrl+id);
      console.log({ data });
      setFetchData(true)
      return data;
    } catch (error) {
      console.error({ message: "failed delete data.", error });
    }
  };

  const handleSubmit = async (evt) => {
    evt.preventDefault();
    await createData(input);
    setInput("");
  };

  const handleDelete = async (evt) => {
    evt.preventDefault();
    await deleteData(evt.target.data.id)
  };

  return (
    <>
      <div className="h-100 w-full flex items-center justify-center bg-teal-lightest font-sans">
        <div className="rounded shadow p-6 m-4 w-full lg:w-3/4 lg:max-w-lg bg-fuchsia-50">
          <div className="mb-4">
            <h1 className="text-grey-darkest text-lg">Todo List</h1>
            <form onSubmit={handleSubmit}>
              <div className="flex mt-4">
                <input
                  className="shadow appearance-none border rounded w-full py-2 px-3 mr-4 text-grey-darker"
                  placeholder="Add Todo"
                  value={input}
                  onChange={(evt) => setInput(evt.target.value)}
                />
                <button
                  type="submit"
                  className="flex-no-shrink p-2 border-2 rounded text-teal border-teal hover:text-white hover:bg-teal-500"
                >
                  Add
                </button>
              </div>
            </form>
          </div>
          <div>
            {todos.length > 0 &&
              todos.map(function (item) {
                return (
                  <div key={item.id} className="flex mb-2 items-center">
                    {/* <input
                      className="mr-4"
                      type="checkbox"
                      name=""
                      checked={item.is_completed}
                    /> */}
                    <p className='w-full text-green text-left'>
                      {item.data}
                    </p>
                    <button onClick={() => deleteData(item.id)} data-id={item.id} className="flex-no-shrink p-2 ml-2 border-2 rounded text-red border-red hover:text-white hover:bg-red-500">
                      Delete
                    </button>
                  </div>
                );
              })}
          </div>
        </div>
      </div>
    </>
  );
}

export default App;

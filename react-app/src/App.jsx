import "./App.css";

function App() {
  return (
    <>
      <div className="h-100 w-full flex items-center justify-center bg-teal-lightest font-sans">
        <div className="rounded shadow p-6 m-4 w-full lg:w-3/4 lg:max-w-lg bg-fuchsia-50">
          <div className="mb-4">
            <h1 className="text-grey-darkest text-lg">Todo List</h1>
            <div className="flex mt-4">
              <input
                className="shadow appearance-none border rounded w-full py-2 px-3 mr-4 text-grey-darker"
                placeholder="Add Todo"
              />
              <button className="flex-no-shrink p-2 border-2 rounded text-teal border-teal hover:text-white hover:bg-teal-500">
                Add
              </button>
            </div>
          </div>
          <div>
            <div className="flex mb-2 items-center">
              <input className="mr-4" type="checkbox" name="" />
              <p className="w-full text-grey-darkest text-left">Task One</p>
              <button className="flex-no-shrink p-2 ml-2 border-2 rounded text-red border-red hover:text-white hover:bg-red-500">
                Delete
              </button>
            </div>
            <div className="flex mb-2 items-center">
              <input className="mr-4" type="checkbox" name="" />
              <p className="w-full line-through text-green text-left">
                Task Two
              </p>
              <button className="flex-no-shrink p-2 ml-2 border-2 rounded text-red border-red hover:text-white hover:bg-red-500">
                Delete
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default App;

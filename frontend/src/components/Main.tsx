const Main = () => {
  return (
    <div className="w-full flex justify-center items-center mt-10">
      <div className="w-[75%]">
        <h1 className="text-3xl font-bold">Create a Memory</h1>
        <div className="w-[40%] flex flex-col gap-5 mt-10">
          <div className="flex-col">
            <h1 className="font-bold">Title</h1>
            <input
              type="text"
              className="w-full bg-gray-100 p-2 mt-1 rounded"
              placeholder="Give Your Memory title"
            />
          </div>
          <div className="flex-col">
            <h1 className="font-bold">Text</h1>
            <input
              type="text"
              className="w-full bg-gray-100 h-[100px] p-2 mt-1 rounded"
              placeholder="Describe Your Memory in Detail."
            />
          </div>
          <div className="flex-col">
            <h1 className="font-bold">Audio</h1>
            <input
              type="file"
              className="w-full bg-gray-100 p-2 mt-1 rounded"
              placeholder="Describe Your Memory in Detail."
            />
          </div>
        </div>
        <div className="flex-col mt-5">
          <h1 className="font-bold">Image</h1>
          <input
            type="file"
            className="w-full bg-gray-100 h-[200px] p-2 mt-1 rounded"
            placeholder="Describe Your Memory in Detail."
          />
        </div>
        <div className="w-full mt-3 flex justify-center items-center">
          <button className="border px-2 py-1 rounded bg-black text-white">Process it!</button>
        </div>
      </div>
    </div>
  );
};

export default Main;

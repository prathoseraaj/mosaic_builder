const Main = () => {
  return (
    <div className="w-full flex justify-center items-center mt-10">
      <div className="w-[75%]">
        <h1 className="text-3xl font-bold">Create a Memory</h1>
        <div className="flex flex-row gap-24">
          <div className="w-[40%] flex flex-col gap-5 mt-10">

            <div className="flex-col">
              <h1 className="font-bold">Description</h1>
              <textarea
                className="w-full bg-gray-100 h-[100px] p-2 mt-1 rounded resize-none"
                placeholder="Describe Your Memory in Detail."
              />
            </div>
                        <div className="flex-col">
              <h1 className="font-bold">People Involved(optional)</h1>
              <input
                type="text"
                className="w-full bg-gray-100 p-2 mt-1 rounded"
                placeholder="Who was with you?"
              />
            </div>
          </div>
          <div className="w-[50%] mt-5">
            <div className="flex-col mt-5">
              <h1 className="font-bold mb-1">Audio</h1>
              <div className="flex flex-col items-center gap-6 rounded-lg border-2 border-dashed border-[#e4e0dd] px-20  py-8">
                <div className="flex max-w-[480px] flex-col items-center gap-2">
                  <p className="text-[#171412] text-lg font-bold leading-tight tracking-[-0.015em] max-w-[480px] text-center">
                    Drag and drop audio file here
                  </p>
                  <p className="text-[#171412] text-sm font-normal leading-normal max-w-[480px] text-center">
                    Or click to browse your audio file
                  </p>
                </div>

                <input
                  type="file"
                  id="audioInput"
                  accept="audio/*"
                  className="hidden"
                />

                <label
                  htmlFor="audioInput"
                  className="flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-10 px-4 bg-[#f4f2f1] text-[#171412] text-sm font-bold leading-normal tracking-[0.015em]"
                >
                  <span className="truncate">Upload</span>
                </label>
              </div>
            </div>
          </div>
        </div>

        <div className="flex flex-col mt-5">
          <h1 className="font-bold mb-1">Image</h1>
          <div className="flex flex-col items-center gap-6 rounded-lg border-2 border-dashed border-[#e4e0dd] px-5 py-10">
            <div className="flex max-w-[480px] flex-col items-center gap-2">
              <p className="text-[#171412] text-lg font-bold leading-tight tracking-[-0.015em] max-w-[480px] text-center">
                Drag and drop files here
              </p>
              <p className="text-[#171412] text-sm font-normal leading-normal max-w-[480px] text-center">
                Or click to browse your files
              </p>
            </div>
            <input type="file" id="fileInput" className="hidden" />
            <label
              htmlFor="fileInput"
              className="flex min-w-[84px] max-w-[480px] cursor-pointer items-center justify-center overflow-hidden rounded-lg h-10 px-4 bg-[#f4f2f1] text-[#171412] text-sm font-bold leading-normal tracking-[0.015em]"
            >
              <span className="truncate">Upload</span>
            </label>
          </div>
        </div>
        <div className="w-full mt-10 flex justify-center items-center">
          <button className="border px-2 py-1 rounded bg-black text-white">
            Process it!
          </button>
        </div>
      </div>
    </div>
  );
};

export default Main;

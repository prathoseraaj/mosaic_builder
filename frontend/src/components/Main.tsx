import axios from "axios";
import { useState } from "react";

const Main = () => {
  const [description, setDescription] = useState("");
  const [audioFile, setAudioFile] = useState<File | null>(null);
  const [imageFile, setImageFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState<string | null>(null);

  const handleSumbit = async (
    e: React.FormEvent<HTMLFormElement>
  ): Promise<void> => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    setError(null);

    const formData = new FormData();
    formData.append("description", description);
    if (audioFile) formData.append("audioFile", audioFile);
    if (imageFile) formData.append("imageFile", imageFile);

    try {
      const response = await axios.post("https://", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(response.data);
    } catch (error: any) {
      setError("Failed to process memory. " + (error?.message || ""));
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="w-full flex justify-center items-center mt-10">
      {!result ? (
        <div className="w-[75%]">
          <h1 className="text-3xl font-bold">Create a Memory</h1>
          <form onSubmit={handleSumbit}>
            <div className="flex flex-row gap-24">
              <div className="w-[40%] flex flex-col gap-5 mt-10">
                <div className="flex-col">
                  <h1 className="font-bold">Description</h1>
                  <textarea
                    className="w-full bg-gray-100 h-[100px] p-2 mt-1 rounded resize-none"
                    placeholder="Describe Your Memory in Detail."
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
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
                      onChange={(e) => {
                        if (e.target.files && e.target.files[0]) {
                          setAudioFile(e.target.files[0]);
                        }
                      }}
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
                <input
                  type="file"
                  id="fileInput"
                  className="hidden"
                  accept="image/*"
                  onChange={(e) => {
                    if (e.target.files && e.target.files[0]) {
                      setImageFile(e.target.files[0]);
                    }
                  }}
                />
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
          </form>
        </div>
      ) : (
        <div className="w-[75%]">
          <h1 className="text-3xl font-bold">Your Story</h1>
          <p className="mt-5 text-gray-800">
            Here's the story generated from your memory upload. We hope you
            enjoy reading it and reliving the moment.
          </p>
          <div className="flex flex-col mt-10">
            <h2 className="text-2xl font-bold">Story Title</h2>
            <p className="mt-3 w-[70%]">
              Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi
              dolorum, neque repellat mollitia modi molestiae impedit voluptas
              rerum pariatur possimus rem asperiores reprehenderit inventore
              nisi quas doloremque quisquam eius labore. Lorem ipsum dolor sit
              amet, consectetur adipisicing elit. Est reiciendis sint magni, cum
              sit libero eos asperiores! Hic aspernatur asperiores excepturi,
              temporibus libero nesciunt dignissimos sequi! Vero deserunt fuga
              consequatur. Lorem ipsum dolor sit amet consectetur adipisicing
              elit. Accusamus inventore sapiente, dolore dolor laborum tempore
              quos est nobis aspernatur in numquam officiis modi eligendi animi
              quae magni rem dicta placeat! Lorem, ipsum dolor sit amet
              consectetur adipisicing elit. Nostrum, repellendus quidem totam
              possimus velit nihil, magni sequi culpa sapiente dignissimos vitae
              numquam, a voluptate aspernatur error? Possimus ratione recusandae
              animi? Lorem ipsum dolor sit amet consectetur adipisicing elit.
              Perspiciatis, quae, modi temporibus possimus saepe laborum
              eveniet, delectus a nisi beatae rem quas? Enim doloribus
              voluptatem accusamus consequuntur adipisci repellendus ex. Lorem
              ipsum dolor sit, amet consectetur adipisicing elit. Explicabo in
              veniam voluptatibus? Nulla cupiditate quaerat iure iste fugit,
              tenetur laudantium eveniet dolor expedita. Nobis est deleniti
              fugiat eum esse asperiores.
            </p>
          </div>
          <div className="w-full mt-10 flex  items-center">
            <button className="border px-2 py-1 rounded bg-black text-white">
              Another Memory
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default Main;

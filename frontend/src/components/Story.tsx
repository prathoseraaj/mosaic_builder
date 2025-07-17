const Story = () => {
  return (
    <div className="w-full flex justify-center items-center mt-10">
      <div className="w-[75%]">
        <h1 className="text-3xl font-bold">Your Story</h1>
        <p className="mt-5 text-gray-800">
          Here's the story generated from your memory upload. We hope you enjoy
          reading it and reliving the moment.
        </p>
        <div className="flex flex-col mt-10">
          <h2 className="text-2xl font-bold">Story Title</h2>
          <p className="mt-3 w-[70%]">
            Lorem ipsum dolor sit amet, consectetur adipisicing elit. Animi
            dolorum, neque repellat mollitia modi molestiae impedit voluptas
            rerum pariatur possimus rem asperiores reprehenderit inventore nisi
            quas doloremque quisquam eius labore. Lorem ipsum dolor sit amet,
            consectetur adipisicing elit. Est reiciendis sint magni, cum sit
            libero eos asperiores! Hic aspernatur asperiores excepturi,
            temporibus libero nesciunt dignissimos sequi! Vero deserunt fuga
            consequatur. Lorem ipsum dolor sit amet consectetur adipisicing
            elit. Accusamus inventore sapiente, dolore dolor laborum tempore
            quos est nobis aspernatur in numquam officiis modi eligendi animi
            quae magni rem dicta placeat! Lorem, ipsum dolor sit amet
            consectetur adipisicing elit. Nostrum, repellendus quidem totam
            possimus velit nihil, magni sequi culpa sapiente dignissimos vitae
            numquam, a voluptate aspernatur error? Possimus ratione recusandae
            animi? Lorem ipsum dolor sit amet consectetur adipisicing elit.
            Perspiciatis, quae, modi temporibus possimus saepe laborum eveniet,
            delectus a nisi beatae rem quas? Enim doloribus voluptatem accusamus
            consequuntur adipisci repellendus ex. Lorem ipsum dolor sit, amet
            consectetur adipisicing elit. Explicabo in veniam voluptatibus?
            Nulla cupiditate quaerat iure iste fugit, tenetur laudantium eveniet
            dolor expedita. Nobis est deleniti fugiat eum esse asperiores.
          </p>
        </div>
        <div className="w-full mt-10 flex  items-center">
          <button className="border px-2 py-1 rounded bg-black text-white">
            Another Memory
          </button>
        </div>
      </div>
    </div>
  );
};

export default Story;

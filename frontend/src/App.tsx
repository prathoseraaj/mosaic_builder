import Main from "./components/Main"
import Navbar from "./components/Navbar"
/* import Story from "./components/Story" */

const App = () => {
  return (
    <div className="h-[100vh] w-full overflow-hidden">
      <Navbar/>
      <hr  className="mt-2 text-gray-200 font-bold"/>
      <Main/> 
    </div>
  )
}

export default App
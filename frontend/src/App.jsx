import UploadPage from "./pages/UploadPage";
import { Toaster } from "react-hot-toast";

function App() {
  return (
    <>
      <Toaster position="top-right" reverseOrder={false} />
      <UploadPage />
    </>
  );
}

export default App;
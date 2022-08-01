import './App.css';
import ImageSlider from './components/ImageSlider';
import { ImageData } from './components/ImageData';

function App() {
  return <ImageSlider slides={ImageData} />;
}

export default App;

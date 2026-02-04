import { useEffect, useState } from "react";
import NavBar from "../components/NavBar";
import "../style/Home.css";

function Home() {
  const words = ["Hello;)", "Welcome!"];
  const [text, setText] = useState("");
  const [wordIndex, setWordIndex] = useState(0);
  const [charIndex, setCharIndex] = useState(0);
  const [deleting, setDeleting] = useState(false);

  useEffect(() => {
    const currentWord = words[wordIndex];
    let timer;

    if (!deleting && charIndex < currentWord.length) {
      timer = setTimeout(() => {
        setText(currentWord.slice(0, charIndex + 1));
        setCharIndex(charIndex + 1);
      }, 120);
    } 
    else if (!deleting && charIndex === currentWord.length) {
      timer = setTimeout(() => setDeleting(true), 900);
    } 
    else if (deleting && charIndex > 0) {
      timer = setTimeout(() => {
        setText(currentWord.slice(0, charIndex - 1));
        setCharIndex(charIndex - 1);
      }, 80);
    } 
    else {
      setDeleting(false);
      setWordIndex((wordIndex + 1) % words.length);
    }

    return () => clearTimeout(timer);
  }, [charIndex, deleting, wordIndex]);

  return (
    <div className="home_div">
      <NavBar showLinks={true} />
      <h1 className="home_page">{text}</h1>
      
    </div>
  );
}

export default Home;

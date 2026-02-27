import { useState } from 'react';
const images = ['img1.jpg','img2.jpg','img3.jpg'];
export default function Gallery() {
	const [idx, setIdx] = useState(0);
	return (<div><img src={images[idx]} alt="" /><button onClick={() => setIdx((idx+images.length-1)%images.length)}>Назад</button><button onClick={() => setIdx((idx+1)%images.length)}>Вперед</button></div>);
}
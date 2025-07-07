import React, { useEffect, useState } from 'react';
export default function Courses() {
  const [courses, setCourses] = useState([]);
  const [level, setLevel] = useState('');

  useEffect(() => {
    fetch('http://localhost:8000/api/courses/recommend?score=12')
      .then(res => res.json())
      .then(data => {
        setCourses(data.courses);
        setLevel(data.level);
      });
  }, []);

  return (
    <div className="p-6">
      <h2 className="text-xl font-semibold">Recommended Courses ({level})</h2>
      <ul className="list-disc pl-6">
        {courses.map((course, idx) => <li key={idx}>{course}</li>)}
      </ul>
    </div>
  );
}
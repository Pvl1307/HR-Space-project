import React, {useEffect, useState} from "react";
import axios from "axios";
import ReactDOM from "react-dom";
import {Table} from "reactstrap";
import "bootstrap/dist/css/bootstrap.min.css";


export const App = () => {
    const [vacancies, setVacancies] = useState([]);

    useEffect(() => {
        axios
            .get("/api/vacancy/")
            .then((response) => {
                setVacancies(response.data);
            })
            .catch((error) => {
                console.error(error);
            });
    }, []);

    return (
        <div>
            <h2>Vacancies</h2>
            <Table striped bordered hover>
                <thead>
                <tr>
                    <th>Title</th>
                    <th>Description</th>
                    <th>Salary</th>
                </tr>
                </thead>
                <tbody>
                {vacancies.map((vacancy) => (
                    <tr key={vacancy.id}>
                        <td>{vacancy.title}</td>
                        <td>{vacancy.description}</td>
                        <td>{vacancy.salary}</td>
                    </tr>
                ))}


                </tbody>
            </Table>
        </div>
    );
};

ReactDOM.render(<App/>, document.getElementById("vacancy-list"));

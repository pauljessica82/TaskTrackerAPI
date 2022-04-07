
import { useState, useEffect } from 'react'
import { BrowserRouter as Router, Route , Routes} from 'react-router-dom'
import Header from './components/Header'
import Tasks from './components/Tasks'
import AddTask from './components/AddTask'
import Footer from './components/Footer'
import About from './components/About'
import { config, detailRoute } from './config'




const App = () => {
	const [showAddTask, setShowAddTask] = useState (true)
	const [tasks, setTasks] = useState([])

	useEffect(() => {
		const getTasks = async () => {
			const tasksFromServer = await fetchTasks()
			setTasks(tasksFromServer)
		}

		getTasks()

	}, [])

	//Fetch task
	const fetchTasks = async () => {
			const res = await fetch(config.url.BASE_API)
			const data = await res.json()

			return data
	}

	//Fetch task with id 
	const fetchTask = async (id) => {

		const res = await fetch(detailRoute(id))
		const data = await res.json()

		return data
	}
    
	//Add Task
	const addTask = async (task) => {
		const res = await fetch(config.url.BASE_API, {
			method: 'POST',
			headers: {
				'Content-type' : 'application/json'
			},

			body: JSON.stringify(task)
		})

		const data = await res.json()

		setTasks([...tasks, data])


    }

	// Delete task
	const deleteTask = async (id) => {
		await fetch(detailRoute(id), {
			method: 'DELETE', 
        })
		setTasks(tasks.filter((task) => task.id !== id ))}

	// Toggle Reminder
	const toggleReminder = async (id) => {
		const taskToToggle = await fetchTask(id)
		const updTask = {
			...taskToToggle,
			reminder: !taskToToggle.reminder
		}
		const res = await fetch(detailRoute(id), {
			method: 'PUT',
			headers: {
				'Content-type': 'application/json',
			},
			body: JSON.stringify(updTask),
		})

		const data = await res.json()

		setTasks(
			tasks.map((task) =>
			task.id === id ?
			{ ...task, reminder: data.reminder } : task
			))

	}
	return (
	  <Router>
		  <div className="container">
				<Header
					onAdd={() => setShowAddTask (!showAddTask)} showAdd={showAddTask}
				/>
				<Routes>
					<Route path='/' exact element={(
						<>
						{showAddTask && <AddTask onAdd={addTask} />}
						{tasks.length > 0 ? (<Tasks tasks={tasks}
							onDelete={deleteTask}
							onToggle={toggleReminder} />)
							: ('No Tasks to Show')}
						</>
				)}
					/>
					<Route path='/about' element={<About/>} />
				</Routes>
			  <Footer />
			</div>
		</Router>
  )
}

export default App

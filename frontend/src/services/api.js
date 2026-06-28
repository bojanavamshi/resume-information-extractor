import axios from 'axios'

const api = axios.create({
  baseURL: 'http://localhost:5000',
  timeout: 120000,
})

export const extractResume = async (file) => {
  const formData = new FormData()
  formData.append('resume', file)

  const response = await api.post('/extract', formData, {
    headers: {
      'Content-Type': 'multipart/form-data',
    },
  })

  return response.data
}

export default api

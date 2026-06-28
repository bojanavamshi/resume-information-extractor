import { useMemo, useRef, useState } from 'react'

function UploadResume({ onUpload, isLoading, onError }) {
  const [selectedFile, setSelectedFile] = useState(null)
  const [dragActive, setDragActive] = useState(false)
  const inputRef = useRef(null)

  const fileLabel = useMemo(() => {
    if (!selectedFile) return 'No file selected'
    return selectedFile.name
  }, [selectedFile])

  const handleFileSelection = (files) => {
    const file = files?.[0]
    if (!file) return

    const acceptedTypes = [
      'application/pdf',
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    ]

    const isAccepted = acceptedTypes.includes(file.type) || /\.(pdf|docx)$/i.test(file.name)

    if (!isAccepted) {
      onError?.('Please upload a PDF or DOCX file only.')
      return
    }

    setSelectedFile(file)
    onError?.('')
  }

  const onDrop = (event) => {
    event.preventDefault()
    setDragActive(false)
    handleFileSelection(event.dataTransfer.files)
  }

  return (
    <div className="upload-card">
      <div
        className={`dropzone ${dragActive ? 'drag-active' : ''}`}
        onDragOver={(event) => {
          event.preventDefault()
          setDragActive(true)
        }}
        onDragLeave={() => setDragActive(false)}
        onDrop={onDrop}
      >
        <p className="dropzone-title">Drag & drop your resume here</p>
        <p className="dropzone-subtitle">PDF or DOCX · up to 5MB</p>
        <input
          ref={inputRef}
          type="file"
          accept=".pdf,.docx"
          aria-label="Upload resume"
          onChange={(event) => handleFileSelection(event.target.files)}
        />
        <button type="button" className="primary-btn" onClick={() => inputRef.current?.click()}>
          Choose file
        </button>
      </div>

      <div className="file-preview">
        <span>Selected file:</span>
        <strong>{fileLabel}</strong>
      </div>

      <button
        type="button"
        className="primary-btn full-width"
        disabled={!selectedFile || isLoading}
        onClick={() => onUpload(selectedFile)}
      >
        {isLoading ? 'Analyzing…' : 'Analyze Resume'}
      </button>
    </div>
  )
}

export default UploadResume

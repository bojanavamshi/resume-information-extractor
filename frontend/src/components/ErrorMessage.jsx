function ErrorMessage({ title = 'Something went wrong', message, onRetry }) {
  return (
    <div className="error-card" role="alert">
      <div className="error-icon">⚠️</div>
      <h3>{title}</h3>
      <p>{message}</p>
      {onRetry && (
        <button type="button" className="secondary-btn" onClick={onRetry}>
          Try again
        </button>
      )}
    </div>
  )
}

export default ErrorMessage

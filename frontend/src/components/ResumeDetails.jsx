function ResumeDetails({ title, icon, items }) {
  const content = Array.isArray(items) ? items : [items]

  return (
    <article className="info-card glass-card">
      <div className="card-title-row">
        <span className="card-icon">{icon}</span>
        <h3>{title}</h3>
      </div>
      <ul className="detail-list">
        {content.map((item, index) => {
          if (typeof item === 'string') {
            return <li key={`${title}-${index}`}>{item}</li>
          }

          return (
            <li key={`${item.label}-${index}`}>
              <span className="detail-label">{item.label}</span>
              <span className="detail-value">{item.value}</span>
            </li>
          )
        })}
      </ul>
    </article>
  )
}

export default ResumeDetails

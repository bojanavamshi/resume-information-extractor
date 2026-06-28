function SkillsCard({ skills }) {
  const skillList = Array.isArray(skills) ? skills : []

  return (
    <article className="info-card glass-card skill-card">
      <div className="card-title-row">
        <span className="card-icon">🛠️</span>
        <h3>Skills</h3>
      </div>
      <div className="skill-grid">
        {skillList.length > 0 ? (
          skillList.map((skill) => (
            <span key={skill} className="skill-chip">
              {skill}
            </span>
          ))
        ) : (
          <p>No skills available.</p>
        )}
      </div>
    </article>
  )
}

export default SkillsCard

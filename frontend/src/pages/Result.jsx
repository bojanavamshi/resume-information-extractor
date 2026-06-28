import { useLocation, Link } from 'react-router-dom'
import ResumeDetails from '../components/ResumeDetails'
import SkillsCard from '../components/SkillsCard'

const sampleData = {
  fullName: 'Ava Patel',
  email: 'ava.patel@email.com',
  phoneNumber: '+1 555 0147',
  skills: ['React', 'Node.js', 'Python', 'MongoDB', 'UI Design'],
  education: ['B.Tech in Computer Science, 2022'],
  experience: ['Senior Frontend Engineer, Acme Corp (2022-Present)'],
  projects: ['Resume Intelligence Platform'],
  certifications: ['AWS Certified Cloud Practitioner'],
  languages: ['English', 'Hindi', 'French'],
  summary:
    'Product-minded engineer with experience building polished, scalable web applications and leading frontend architecture initiatives.',
}

function Result() {
  const location = useLocation()
  const resumeData = location.state?.resumeData || sampleData

  const sections = [
    {
      title: 'Contact',
      icon: '👤',
      items: [
        { label: 'Full Name', value: resumeData.fullName || 'Not provided' },
        { label: 'Email', value: resumeData.email || 'Not provided' },
        { label: 'Phone', value: resumeData.phoneNumber || 'Not provided' },
      ],
    },
    {
      title: 'Education',
      icon: '🎓',
      items: resumeData.education || ['Not provided'],
    },
    {
      title: 'Experience',
      icon: '💼',
      items: resumeData.experience || ['Not provided'],
    },
    {
      title: 'Projects',
      icon: '🧩',
      items: resumeData.projects || ['Not provided'],
    },
    {
      title: 'Certifications',
      icon: '🏅',
      items: resumeData.certifications || ['Not provided'],
    },
    {
      title: 'Languages',
      icon: '🌐',
      items: resumeData.languages || ['Not provided'],
    },
  ]

  return (
    <section className="result-section">
      <div className="section-heading">
        <div>
          <p className="eyebrow">Resume analysis complete</p>
          <h2>Here is a structured summary of your resume.</h2>
        </div>
        <Link className="secondary-link" to="/">
          Upload another resume
        </Link>
      </div>

      <div className="summary-card glass-card">
        <h3>Professional Summary</h3>
        <p>{resumeData.summary || 'No summary available yet.'}</p>
      </div>

      <div className="result-grid">
        {sections.map((section) => (
          <ResumeDetails
            key={section.title}
            title={section.title}
            icon={section.icon}
            items={section.items}
          />
        ))}
      </div>

      <SkillsCard skills={resumeData.skills || []} />
    </section>
  )
}

export default Result

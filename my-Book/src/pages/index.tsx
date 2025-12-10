import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className={clsx('hero__title', styles.heroTitle)}>
          Physical AI & Humanoid Robotics
        </Heading>
        <p className={clsx('hero__subtitle', styles.heroSubtitle)}>
          A comprehensive guide exploring how AI-powered humanoid robots think, move, and interact with the physical world.
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--primary button--lg"
            to="/docs/introduction/intro">
            Get Started →
          </Link>
        </div>
      </div>
    </header>
  );
}

const ValuePropList = [
    {
        title: 'Simulation First',
        icon: '💻',
        description:
            'Master digital twins and physics-based simulation to test, train, and validate robots in virtual environments before deploying to hardware.',
    },
    {
        title: 'Hands-On ROS2',
        icon: '🤖',
        description:
            'Go from zero to hero with the Robot Operating System (ROS2). Learn to build and manage complex robotics applications like a pro.',
    },
    {
        title: 'AI-Powered Perception',
        icon: '👁️',
        description:
            'Implement advanced perception systems using synthetic data and techniques like Visual SLAM for robust navigation and interaction.',
    },
];

const ModuleList = [
  {
    title: 'Module 1: ROS2 Foundations',
    description: 'Build a strong foundation in the Robot Operating System, the standard for modern robotics.',
    link: '/docs/module-1-ros2/ros-architecture',
  },
  {
    title: 'Module 2: Digital Twin & Simulation',
    description: 'Master Unity for physics-based simulation and sensor modeling.',
    link: '/docs/module-2-digital-twin/digital-twin-concept',
  },
  {
    title: 'Module 3: NVIDIA Isaac',
    description: 'Dive into advanced AI for robotics with NVIDIA\'s powerful tools for perception and navigation.',
    link: '/docs/module-3-nvidia-isaac/what-is-isaac',
  },
  {
    title: 'Module 4: Vision-Language Agents',
    description: 'Build a capstone project using cutting-edge VLAs for voice-to-action robot control.',
    link: '/docs/module-4-vla-capstone/capstone',
  },
];

const StatList = [
    {
        number: '04',
        label: 'Core Modules',
    },
    {
        number: '10+',
        label: 'Projects & Labs',
    },
    {
        number: '01',
        label: 'Capstone Project',
    },
];

function ValueProp({ title, icon, description }) {
    return (
        <div className={clsx('col col--4', styles.valueProp)}>
            <div className={clsx('card', styles.valuePropCard)}>
                <div className={styles.valuePropIcon}>{icon}</div>
                <div className="card__body">
                    <Heading as="h3" className={styles.valuePropTitle}>{title}</Heading>
                    <p>{description}</p>
                </div>
            </div>
        </div>
    );
}

function Module({ title, description, link }) {
  return (
    <Link to={link} className={styles.moduleLink}>
      <div className={clsx('card', styles.moduleCard)}>
          <div className="card__body">
              <Heading as="h3" className={styles.moduleTitle}>{title}</Heading>
              <p className={styles.moduleDescription}>{description}</p>
          </div>
      </div>
    </Link>
  );
}

function Stat({ number, label }) {
    return (
        <div className={clsx('col', styles.statItem)}>
            <div className={styles.statNumber}>{number}</div>
            <div className={styles.statLabel}>{label}</div>
        </div>
    );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="A comprehensive guide exploring how AI-powered humanoid robots think, move, and interact with the physical world.">
      <HomepageHeader />
      <main className={styles.mainContent}>
        <section className={styles.section}>
            <div className="container">
                <div className="row">
                    {ValuePropList.map((props, idx) => (
                        <ValueProp key={idx} {...props} />
                    ))}
                </div>
            </div>
        </section>

        <section className={clsx(styles.section, styles.sectionAlt)}>
          <div className="container">
            <Heading as="h2" className={clsx('text--center', styles.sectionTitle)}>
              A Structured Learning Path
            </Heading>
            <p className={clsx('text--center', styles.sectionSubtitle)}>
                From fundamentals to advanced AI, our curriculum is designed to build your expertise step-by-step.
            </p>
            <div className={styles.moduleGrid}>
              {ModuleList.map((props, idx) => (
                <Module key={idx} {...props} />
              ))}
            </div>
          </div>
        </section>

        <section className={styles.section}>
            <div className="container">
                <div className={clsx('row', styles.statsContainer)}>
                    {StatList.map((props, idx) => (
                        <Stat key={idx} {...props} />
                    ))}
                </div>
            </div>
        </section>

      </main>
    </Layout>
  );
}

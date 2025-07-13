# CRM Lite

A modern, lightweight Customer Relationship Management (CRM) system built with Next.js, TypeScript, and Tailwind CSS. Perfect for small businesses and freelancers to manage clients, projects, and invoices.

## ✨ Features

- **Client Management** - Add, edit, and organize your client information
- **Project Tracking** - Monitor project status and progress
- **Invoice Generation** - Create and manage invoices with automatic calculations
- **Dashboard Analytics** - Get insights into your business performance
- **Responsive Design** - Works seamlessly on desktop and mobile devices
- **Modern UI** - Clean, professional interface built with shadcn/ui components

## 🚀 Tech Stack

- **Frontend**: Next.js 13, React 18, TypeScript
- **Styling**: Tailwind CSS, shadcn/ui components
- **State Management**: Zustand with persistence
- **Icons**: Lucide React
- **Backend**: FastAPI (Python) - *Optional, can work with mock data*
- **Database**: SQLite (for backend)

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CRM-Lite.git
   cd CRM-Lite
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Run the development server**
   ```bash
   npm run dev
   ```

4. **Open your browser**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 🔧 Configuration

### Frontend Only (Mock Data)
The application works out of the box with mock data. No additional configuration needed.

### With Backend (Optional)
If you want to use the FastAPI backend:

1. **Install Python dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Run the backend server**
   ```bash
   python main.py
   ```

3. **Update environment variables**
   Create a `.env.local` file in the root directory:
   ```env
   NEXT_PUBLIC_API_URL=http://localhost:8000
   ```

## 📱 Usage

### Getting Started
1. **Register/Login** - Create an account or sign in
2. **Add Clients** - Start by adding your clients with their contact information
3. **Create Projects** - Assign projects to clients and track their progress
4. **Generate Invoices** - Create professional invoices with itemized billing
5. **Monitor Dashboard** - View your business metrics and recent activity

### Key Features

#### Client Management
- Add client contact information
- Track client companies and details
- Search and filter clients
- Edit and update client information

#### Project Tracking
- Create projects linked to clients
- Set project status (Pending, Ongoing, Completed)
- Add project descriptions and details
- Monitor project timelines

#### Invoice Generation
- Create detailed invoices with multiple line items
- Automatic tax calculations (9% default)
- Track payment status (Paid, Unpaid, Overdue)
- Set due dates and invoice numbers

#### Dashboard Analytics
- View total clients, active projects, and revenue
- Monitor unpaid invoices
- See recent activity and trends
- Performance metrics with visual indicators

## 🎨 UI Components

Built with modern, accessible components:
- **Cards** - Clean content containers
- **Tables** - Responsive data display
- **Forms** - User-friendly input handling
- **Dialogs** - Modal interactions
- **Badges** - Status indicators
- **Buttons** - Consistent action elements

## 📁 Project Structure

```
CRM-Lite/
├── app/                    # Next.js app directory
│   ├── dashboard/         # Dashboard page
│   ├── clients/           # Client management
│   ├── projects/          # Project tracking
│   ├── invoices/          # Invoice generation
│   ├── login/             # Authentication
│   └── register/          # User registration
├── components/            # Reusable components
│   ├── ui/               # shadcn/ui components
│   └── layout/           # Layout components
├── lib/                  # Utilities and API
│   ├── api.ts           # API functions
│   ├── auth.ts          # Authentication store
│   └── utils.ts         # Helper functions
├── backend/              # FastAPI backend (optional)
│   ├── main.py          # FastAPI application
│   ├── database.py      # Database setup
│   ├── auth.py          # Authentication logic
│   └── schemas.py       # Pydantic models
└── public/              # Static assets
```

## 🔐 Authentication

- **Secure Login/Registration** - JWT-based authentication
- **Protected Routes** - Automatic redirection for unauthenticated users
- **Persistent Sessions** - Stay logged in across browser sessions
- **User Management** - Profile settings and preferences

## 📊 Data Models

### Client
- Name, email, phone, company
- Creation and update timestamps
- Associated projects and invoices

### Project
- Name, description, status
- Client association
- Timeline tracking

### Invoice
- Invoice number, items, amounts
- Tax calculations, due dates
- Payment status tracking
- Client and project links

## 🚀 Deployment

### Netlify (Recommended)
1. Connect your GitHub repository to Netlify
2. Set build command: `npm run build`
3. Set publish directory: `out`
4. Deploy automatically on push

### Vercel
1. Import project from GitHub
2. Configure build settings
3. Deploy with zero configuration

### Manual Deployment
```bash
npm run build
npm run export
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🐛 Bug Reports

If you find a bug, please create an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable

## 💡 Feature Requests

We welcome feature requests! Please create an issue with:
- Clear description of the feature
- Use case and benefits
- Any implementation ideas

## 📞 Support

- **Documentation**: Check this README and code comments
- **Issues**: Create a GitHub issue for bugs or questions
- **Discussions**: Use GitHub Discussions for general questions

## 🙏 Acknowledgments

- [Next.js](https://nextjs.org/) - React framework
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS
- [shadcn/ui](https://ui.shadcn.com/) - Beautiful UI components
- [Lucide](https://lucide.dev/) - Icon library
- [Zustand](https://github.com/pmndrs/zustand) - State management

---

**CRM Lite** - Simplifying business management, one client at a time. 🚀

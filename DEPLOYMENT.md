# StockLift Vercel Deployment Guide

This guide will help you deploy StockLift on Vercel step by step.

## Prerequisites

- GitHub repository with your StockLift code
- Vercel account (free tier available)
- Google API key (for location services)

## Step-by-Step Deployment

### 1. Repository Preparation

Ensure your repository has these files:
```
StockLift-ScriptedByHer/
├── app.py              # Main Flask application
├── vercel.json         # Vercel configuration
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python version
├── .gitignore         # Git ignore file
└── models/            # ML models directory
```

### 2. Vercel Setup

1. **Sign up/Login to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign in with GitHub

2. **Create New Project**
   - Click "New Project"
   - Import your GitHub repository
   - Vercel will auto-detect Python/Flask

3. **Configure Project Settings**
   - **Framework Preset**: Other
   - **Root Directory**: `./` (or leave empty)
   - **Build Command**: Leave empty (auto-detected)
   - **Output Directory**: Leave empty (auto-detected)
   - **Install Command**: `pip install -r requirements.txt`

### 3. Environment Variables

Add this in Vercel project settings → Environment Variables:

```bash
GOOGLE_API_KEY=your-google-api-key
```

**For Local Development:**
```bash
export GOOGLE_API_KEY=your-google-api-key
```

**Quick Start:**
```bash
export GOOGLE_API_KEY=your-google-api-key
python app.py
```

### 4. Deploy

1. Click "Deploy" button
2. Wait for build to complete (2-5 minutes)
3. Your app will be live at `https://your-project-name.vercel.app`

### 5. Post-Deployment

#### Check Deployment
- Visit your app URL
- Test main features:
  - Product health analysis
  - Festival recommendations
  - Photogenix AI (image processing)

#### Monitor Logs
- Go to Vercel dashboard → Functions
- Check for any errors in deployment logs

## Troubleshooting

### Common Issues

1. **Build Fails**
   - Check `requirements.txt` for missing dependencies
   - Ensure Python version in `runtime.txt` is supported
   - Check Vercel build logs for specific errors

2. **App Not Loading**
   - Verify `vercel.json` configuration
   - Check environment variables are set correctly
   - Ensure `app.py` is the main entry point

3. **File Upload Issues**
   - Vercel uses `/tmp` for temporary storage
   - Files are not persistent between requests
   - Consider using external storage (AWS S3, etc.)

4. **ML Model Loading**
   - Models are loaded on each request
   - Consider model caching or external ML services
   - Check model file sizes (Vercel has limits)

### Performance Optimization

1. **Reduce Bundle Size**
   - Remove unused dependencies
   - Optimize ML model sizes
   - Use CDN for static assets

2. **Improve Load Times**
   - Cache frequently used data
   - Optimize database queries
   - Use lazy loading for ML models

## Production Considerations

### Database
- Use external database (MongoDB Atlas, PostgreSQL)
- Don't rely on local SQLite files
- Set up proper connection pooling

### File Storage
- Use cloud storage (AWS S3, Google Cloud Storage)
- Implement proper file upload handling
- Set up CDN for static assets

### Monitoring
- Set up Vercel Analytics
- Monitor function execution times
- Set up error tracking (Sentry, etc.)

### Security
- Use strong secret keys
- Implement proper authentication
- Validate all user inputs
- Use HTTPS (automatic with Vercel)

## Custom Domain Setup

1. **Add Domain in Vercel**
   - Go to project settings → Domains
   - Add your custom domain
   - Follow DNS configuration instructions

2. **SSL Certificate**
   - Vercel provides automatic SSL
   - No additional configuration needed

## Scaling

### Vercel Plans
- **Hobby**: 10s execution limit, 100GB bandwidth
- **Pro**: 15s execution limit, 1TB bandwidth
- **Enterprise**: Custom limits

### When to Upgrade
- High traffic volume
- Complex ML operations
- Long-running processes
- Custom domain requirements

## Support

If you encounter issues:
1. Check Vercel documentation
2. Review deployment logs
3. Test locally first
4. Contact Vercel support if needed

---

**Happy Deploying! 🚀** 
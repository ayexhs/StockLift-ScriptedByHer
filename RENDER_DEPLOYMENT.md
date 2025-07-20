# StockLift Deployment Guide for Render.com

This guide will help you deploy your StockLift application on Render.com, a cloud platform that supports Python applications with generous free tiers.

## Prerequisites

1. **GitHub Account**: Your code should be in a GitHub repository
2. **Render Account**: Sign up at [render.com](https://render.com)
3. **Google API Key**: For Photogenix AI features (optional but recommended)

## Step 1: Prepare Your Repository

Ensure your repository has these files:
- `app.py` (main Flask application)
- `requirements.txt` (Python dependencies)
- `build.sh` (build script - already created)
- `render.yaml` (Render configuration - already created)

## Step 2: Deploy on Render

### Option A: Using render.yaml (Recommended)

1. **Connect GitHub Repository**:
   - Go to [render.com](https://render.com) and sign in
   - Click "New +" and select "Blueprint"
   - Connect your GitHub account if not already connected
   - Select your StockLift repository

2. **Deploy with Blueprint**:
   - Render will automatically detect the `render.yaml` file
   - Click "Apply" to deploy
   - The deployment will start automatically

### Option B: Manual Deployment

1. **Create New Web Service**:
   - Go to [render.com](https://render.com) and sign in
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository

2. **Configure Service**:
   - **Name**: `stocklift-app`
   - **Environment**: `Python 3`
   - **Build Command**: `chmod +x build.sh && ./build.sh`
   - **Start Command**: `gunicorn app:app`

3. **Set Environment Variables**:
   - Click "Environment" tab
   - Add these variables:
     - `PYTHON_VERSION`: `3.9.16`
     - `FLASK_ENV`: `production`
     - `FLASK_DEBUG`: `false`
     - `GOOGLE_API_KEY`: `your-google-api-key` (optional)

4. **Deploy**:
   - Click "Create Web Service"
   - Render will start building and deploying your app

## Step 3: Configure Environment Variables

### Required Variables

1. **GOOGLE_API_KEY** (Optional but recommended):
   - Go to [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key
   - Add it to your Render environment variables

### Optional Variables

- `FLASK_SECRET_KEY`: A random secret key for sessions
- `DATABASE_URL`: If you want to use an external database

## Step 4: Monitor Deployment

1. **Check Build Logs**:
   - Go to your service dashboard
   - Click "Logs" to see build and runtime logs
   - Monitor for any errors during deployment

2. **Verify Deployment**:
   - Once deployed, click the provided URL
   - Test the main features:
     - Homepage loads
     - Festival dashboard works
     - Shopkeeper login functions
     - Photogenix AI features (if API key is set)

## Step 5: Custom Domain (Optional)

1. **Add Custom Domain**:
   - Go to your service settings
   - Click "Custom Domains"
   - Add your domain name
   - Configure DNS as instructed

## Troubleshooting

### Common Issues

1. **Build Fails**:
   - Check `requirements.txt` for version conflicts
   - Ensure all dependencies are compatible
   - Check build logs for specific errors

2. **App Won't Start**:
   - Verify `gunicorn app:app` command
   - Check if port is correctly configured
   - Review runtime logs

3. **File Upload Issues**:
   - Ensure `uploads/` and `processed/` directories exist
   - Check file permissions
   - Verify static file serving

4. **Memory Issues**:
   - Render free tier has memory limits
   - Consider upgrading to paid plan for ML models
   - Optimize image processing for smaller files

### Performance Optimization

1. **Enable Caching**:
   - Add Redis for session storage
   - Implement static file caching
   - Use CDN for static assets

2. **Database Optimization**:
   - Use external database (PostgreSQL on Render)
   - Implement connection pooling
   - Add database indexes

## Post-Deployment

1. **Test All Features**:
   - Product health analysis
   - Festival dashboard
   - Discount calculator
   - Bundle recommendations
   - Photogenix AI
   - Shopkeeper dashboard

2. **Monitor Performance**:
   - Check response times
   - Monitor error rates
   - Track resource usage

3. **Set Up Monitoring**:
   - Enable Render's built-in monitoring
   - Set up alerts for downtime
   - Monitor application logs

## Support

- **Render Documentation**: [docs.render.com](https://docs.render.com)
- **Render Community**: [community.render.com](https://community.render.com)
- **GitHub Issues**: For application-specific issues

## Cost Considerations

- **Free Tier**: 750 hours/month, 512MB RAM, shared CPU
- **Paid Plans**: Start at $7/month for dedicated resources
- **Database**: Free PostgreSQL available
- **Custom Domains**: Free with SSL certificates

Your StockLift application should now be successfully deployed on Render! 🚀 
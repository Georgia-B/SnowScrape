FROM amazonlinux:2023

# Install Python 3.11 and pip
RUN yum install -y python3.11 python3.11-pip

# Install Lambda Runtime Interface Client
RUN pip3.11 install awslambdaric

# Install system dependencies for Playwright/Chromium
RUN yum install -y \
    atk \
    cups-libs \
    gtk3 \
    ipa-gothic-fonts \
    libXcomposite \
    libXcursor \
    libXdamage \
    libXext \
    libXi \
    libXrandr \
    libXScrnSaver \
    libXtst \
    pango \
    xorg-x11-server-Xvfb \
    libdrm \
    mesa-libgbm \
    at-spi2-atk \
    at-spi2-core \
    wget \
    tar \
    gzip \
    && yum clean all

# Install Python dependencies
COPY requirements.txt .
RUN pip3.11 install --upgrade pip && pip3.11 install -r requirements.txt

# Install Playwright browsers
RUN python3.11 -m playwright install

# Copy your code
COPY . .

# Set the Lambda handler
CMD ["awslambdaric", "scrape.lambda_handler"]
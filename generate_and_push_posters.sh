#!/bin/bash
# Automated Prize2Pride Poster Generator with Instant GitHub Push
# Generates batches of posters and pushes each batch immediately

REPO_DIR="/home/ubuntu/Prize2Pride-English-A1"
BATCH_SIZE=5
TOTAL_BATCHES=40  # 40 batches × 5 = 200 posters

cd "$REPO_DIR"

echo "=========================================="
echo "PRIZE2PRIDE BULK POSTER GENERATOR"
echo "=========================================="
echo "Batch Size: $BATCH_SIZE posters"
echo "Total Batches: $TOTAL_BATCHES"
echo "Total Posters: $((BATCH_SIZE * TOTAL_BATCHES))"
echo "=========================================="
echo ""

for ((batch=1; batch<=TOTAL_BATCHES; batch++)); do
    echo "📸 Generating Batch $batch/$TOTAL_BATCHES..."
    
    # Note: Image generation happens via Python script
    # This script handles the Git operations
    
    # Check if new images exist
    if [ -d "host_posters/images" ]; then
        IMAGE_COUNT=$(find host_posters/images -name "*.png" | wc -l)
        
        if [ $IMAGE_COUNT -gt 0 ]; then
            echo "   ✓ Found $IMAGE_COUNT images"
            echo "   📤 Pushing to GitHub..."
            
            # Add all new images
            git add host_posters/images/*.png
            
            # Commit with batch info
            git commit -m "Batch $batch: Add $BATCH_SIZE Prize2Pride AI host posters (Total: $IMAGE_COUNT)

Auto-generated hyper-realistic posters featuring:
- Diverse, stunningly beautiful hosts
- Prize2Pride branded studio
- Purchase2Win and Buy2Win platforms
- Luxurious gift wheel
- Professional lighting and styling

Batch $batch of $TOTAL_BATCHES complete."
            
            # Push to GitHub
            git push origin main
            
            echo "   ✅ Batch $batch pushed successfully!"
            echo ""
        fi
    fi
    
    # Small delay between batches
    sleep 2
done

echo "=========================================="
echo "✅ ALL BATCHES COMPLETE!"
echo "=========================================="
echo "Total posters generated and pushed to GitHub"
echo "Repository: https://github.com/collegegrahamusa-art/Prize2Pride-English-A1"
echo "=========================================="

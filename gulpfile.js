var gulp        = require('gulp'),
    cleanCSS    = require('gulp-clean-css'),
    uglify      = require('gulp-uglify'),
    concat      = require('gulp-concat'),
    buffer      = require('vinyl-buffer'),
    rename      = require('gulp-rename'),
    changed     = require('gulp-changed'),
    browserSync = require('browser-sync');

// Livereload
gulp.task('browser-sync', function() {
  browserSync({
    server: {
      baseDir: "templates/2016/"
    },
    port: process.env.PORT || 3000
  });
});

// Concatena y minifica los archivos CSS para el landing 2015.
gulp.task('concat2015CSS', function() {
  return gulp.src(['main/static/2015/css/bootstrap.min.css',
                   'main/static/2015/css/animate.css',
                   'main/static/2015/css/font-awesome.min.css',
                   'main/static/2015/css/font-lineicons.min.css',
                   'main/static/2015/css/jquery.fancybox.css',
                   ])
    .pipe(buffer())
    .pipe(concat('concat.min.css'))
    .pipe(cleanCSS())
    .pipe(changed('main/static/2015/css/'))
    .pipe(gulp.dest('main/static/2015/css/'));
});

// Concatena y minifica los archivos JS para el landing.
gulp.task('concat2015JS', function() {
  return gulp.src([
                   'main/static/2015/js/jquery.nav.js',
                   'main/static/2015/js/jquery.appear.js',
/*

                   'main/static/2015/js/scripts.min.js',
*/
                 ])
    .pipe(buffer())
    .pipe(concat('concat.min.js'))
    .pipe(uglify())
    .pipe(changed('main/static/2015/js/'))
    .pipe(gulp.dest('main/static/2015/js/'));
});

// Concatena y minifica los archivos CSS para el landing.
gulp.task('concatCSS', function() {
  return gulp.src(['main/static/2016/css/bootstrap.css',
                   'main/static/2016/css/font-awesome.min.css',
                   'main/static/2016/css/reset.css',
                   'main/static/2016/css/layout.css',
                   'main/static/2016/css/font.css',
                   'main/static/2016/css/color.css',
                   'main/static/2016/css/bootstrap-image-gallery.min.css',
                   ])
    .pipe(buffer())
    .pipe(concat('concat.min.css'))
    .pipe(cleanCSS())
    .pipe(changed('main/static/2016/css/'))
    .pipe(gulp.dest('main/static/2016/css/'));
});

// Concatena y minifica los archivos JS para el landing.
gulp.task('concatJS', function() {
  return gulp.src(['main/static/2016/js/jquery-1.11.1.min.js',
                   'main/static/2016/js/bootstrap.min.js',
                   'main/static/2016/js/bootstrap-image-gallery.min.js',
                   'main/static/2016/js/scripts.js',
                 ])
    .pipe(buffer())
    .pipe(concat('concat.min.js'))
    .pipe(uglify())
    .pipe(changed('main/static/2016/js/'))
    .pipe(gulp.dest('main/static/2016/js/'));
});

// Vigila cambios que se produzcan en el código
// y lanza las tareas relacionadas
gulp.task('watch', function() {
  gulp.watch('main/static/2015/css/**/.css', ['concat2015CSS']);
  gulp.watch('main/static/2015/js/*.js', ['concat2015JS']);
  gulp.watch('main/static/2016/css/**/*.css', ['concatCSS']);
  gulp.watch('main/static/2016/js/**/*.js', ['concatJS']);
});

/*gulp.task('default', ["concatCSS", "concatJS", "minifyCSS", "minifyJS"]);*/
gulp.task('default', ["watch"]);

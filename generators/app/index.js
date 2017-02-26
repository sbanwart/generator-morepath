var path = require('path');

var Generator = require('yeoman-generator');

module.exports = class extends Generator {
    constructor(args, opts) {
        super(args, opts);
    }

    prompting() {
        return this.prompt([{
            type: 'input',
            name: 'project_name',
            message: 'Your project name',
            default: this.appname
        }]).then((answers) => {
            this.log('project name', answers.project_name);
            this.props = answers;
        });
    }

    writing() {
        let projName = this.props.project_name;

        this.fs.copyTpl(
            this.templatePath('setup.py'),
            this.destinationPath('setup.py'),
            { project_name: projName }
        );

        this.fs.copyTpl(
            this.templatePath('__init__.py'),
            this.destinationPath(path.join(projName, '__init__.py')),
            { project_name: projName }
        );

        this.fs.copy(
            this.templatePath('__main__.py'),
            this.destinationPath(path.join(projName, '__main__.py'))
        );

        this.fs.copy(
            this.templatePath('app.py'),
            this.destinationPath(path.join(projName, 'app.py'))
        );

        this.fs.copy(
            this.templatePath('model.py'),
            this.destinationPath(path.join(projName, 'model.py'))
        );

        this.fs.copy(
            this.templatePath('path.py'),
            this.destinationPath(path.join(projName, 'path.py'))
        );

        this.fs.copy(
            this.templatePath('view.py'),
            this.destinationPath(path.join(projName, 'view.py'))
        );
    }
};